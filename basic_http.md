# HTTP

Cuando ingresamos el DNS en el Browser y obtenemos una ip del isp podemos enviar una REQUEST.

### REQUEST

Las request tienen VERBO que determina la operacion del request:

GET: pide algun resource al server.
POST: Le pedimos al servidor que acepte algo que enviamos.


### Response

Respuesta a la request. Tiene la siguiente estructura:

* Status line: status code. (basicos)
    * 200 OK
    * 404 NOT FOUND
* Message body: requerimento del usuario.