from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, resource):
    if "x" not in posted_data or "y" not in posted_data:
        return 301
    else:
        if resource == 'divide' and int(posted_data['y']) == 0:
            return 401
        return 200



class Add(Resource):
    def post(self):
        # if I am here, then the resource Add was requested using the method POST
        
        # Step 1: Get posted data:
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data, "add")
        if status_code != 200:
            ret_map = {
            'Message': "An error happened",
            'Status Code': status_code
            }
            return jsonify(ret_map)
        else:
            y = int(posted_data["y"])
            x = int(posted_data['x'])
            ret = x+y
            ret_map = {
            'Message': ret,
            'Status Code': status_code
            }
            return jsonify(ret_map)


class Subtract(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data, "substract")

        if status_code != 200:
            ret_map = {
            'Message': "An error happened",
            'Status Code': status_code
            }
        else:
            y = int(posted_data['y'])
            x = int(posted_data['x'])
            ret = x - y
            ret_map = {
                'Message': ret,
                'Status code': status_code
            }
        return jsonify(ret_map) 

class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data, "multiply")
        
        if status_code != 200:
            ret_map = {
            'Message': "An error happened",
            'Status Code': status_code
            }
        else:
            y = int(posted_data['y'])
            x = int(posted_data['x'])
            ret = x * y
            ret_map = {
                'Message': ret,
                'Status code': status_code
            }
        return jsonify(ret_map)

class Divide(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data, "divide")
        
        if status_code != 200:
            if status_code == 401:
                ret_map = {
                    'Message': "Division by 0",
                    'Status Code': status_code
                }
            else:
                ret_map = {
                    'Message': "An error happened",
                    'Status Code': status_code
            }
        else:
            y = int(posted_data['y'])
            x = int(posted_data['x'])
            ret = x / y
            ret_map = {
                'Message': ret,
                'Status code': status_code
            }
        return jsonify(ret_map)
    

api.add_resource(Add, "/Add")
api.add_resource(Multiply, "/Multiply")
api.add_resource(Subtract, "/Substract")
api.add_resource(Divide, '/Divide')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

