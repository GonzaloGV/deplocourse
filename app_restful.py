from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, resource):
    if resource == 'add':
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
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
            'Status Code': 200
            }
            return jsonify(ret_map)


class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/Add")



if __name__ == '__main__':
    app.run(debug=True)

