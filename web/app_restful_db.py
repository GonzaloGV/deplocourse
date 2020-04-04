"""
1) Registration of a user
2) Each user gets 10 tokents
3) store a sentence on a our database for 1 token
4) Retrieve his stored sentence on out databse for 1 token
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient
import bcrypt
from customExceptions import InvalidCredentials, OutOfTokens

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]

def verify_pw(username, password):
    try:
        hashed_pw = users.find_one({
            "Username":username,
        })['Password']
        if bcrypt.hashpw(password.encode(), hashed_pw) != hashed_pw:
            raise InvalidCredentials('The username or password is wrong')
    except TypeError as e:
        raise InvalidCredentials('The username is doesnt exist.')

def count_tokens(username):
    num_of_tokens = users.find({
        "Username":username
    })[0]['Tokens']

    if num_of_tokens == 0:
        raise OutOfTokens('Out of tokens.')

    return num_of_tokens

class Register(Resource):
    def post(self):
        # Get posted data by the user
        posted_data = request.get_json()

        try:
            username = posted_data['username']
            password = posted_data['password'].encode()
            # hash(password + salt) = wdkfjhwelkfhlk33lk4jh23lk4jh2
            hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

            users.insert({
                "Username": username,
                "Password": hashed_pw,
                "Sentence": "",
                "Tokens": 6,
            })

            response = {
                "status":200,
                "msg": "You successfully signed up."
            }

        except KeyError as e:
            response = {
                'status': 401,
                'Message': 'Need username and password.'
            }

        return response
        
        
class Store(Resource):
    def post(self):

        try:
            # get the posted data
            posted_data = request.get_json()
            username = posted_data["username"]
            password = posted_data["password"]
            sentence = posted_data["sentence"]
            # step 3 verify the username pw match
            verify_pw(username, password)
            num_tokens = count_tokens(username)
           
            # store user setence and take one token
            users.update({
                "Username": username,
            }, {
                "$set": {
                    "Sentence": sentence,
                    "Tokens": num_tokens-1
                    }
            })

            response = {
                "status": 200,
                "msg": "Sentence saved successfully"
            }

        except KeyError as e:
            response = {
                'status': 401,
                'Message': 'Need username and password.'
            }
        except InvalidCredentials as e:
            response = {
                'status': 302,
                'Message': e.message
            }
        except OutOfTokens as e:
            response = {
                'status':301,
                'Message':e.message
            }   
        
        return jsonify(response)

class Retrieve(Resource):
    def post(self):
        try:
            # get the posted data
            posted_data = request.get_json()
            username = posted_data["username"]
            password = posted_data["password"]
            # step 3 verify the username pw match
            verify_pw(username, password)
            num_tokens = count_tokens(username)

            # store user setence and take one token
            sentence = users.find({
                "Username": username,
            })[0]["Sentence"]

            response = {
                "status": 200,
                "msg": sentence
            }
        except KeyError as e:
            response = {
                'status': 401,
                'Message': 'Need username and password.'
            }
        except InvalidCredentials as e:
            response = {
                'status': 302,
                'Message': e.message
            }
        except OutOfTokens as e:
            response = {
                'status':301,
                'Message':e.message
            }   
        
        return jsonify(response)
        


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Retrieve, '/retrieve')

if __name__ == '__main__':
    app.run(host='0.0.0.0')