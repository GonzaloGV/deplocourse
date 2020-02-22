from flask import Flask, jsonify, request

app = Flask('__name__') #App name

# 127.0.0.1:5000/
# cada vez que alguien le pega a la direccion de arriba
# la funcion que esta abajo del decorador se va a hacer 
# cargo de procesar la request
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # Get x, y from the posted data
    data_dict = request.get_json()
    x = data_dict["x"]
    y = data_dict["y"]
    #Add z=x+y
    z = x + y
    #Prepare a JSON, "z":z
    ret_json = {
        "z":z
    }
    #return jsonify(map_prepared)
    return jsonify(ret_json), 200

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

"""

Todas las comunicaciones entre server/server, server/browser, browser/browser
Son en texto! porque TCP solo soporta text
TEXT TCP
[
    123 125 126 127
    124 125 126 127
] esta es una representacion de una imagen

Browser google.com

"""

@app.route('/bye')
def bye():
    # Prerare a response for the request that come to /bye
    c = 2*534
    s = str(c)
    return 'bye'

# En un web service por lo generar las response son JSON
# o otras estructuras de datos semi-estructurada
# En una web application por lo generar se devuelven pages o
# renderiza cosas.

if __name__=="__main__":
    app.run(debug=True)