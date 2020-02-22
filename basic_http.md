# HTTP

Cuando ingresamos el DNS en el Browser y obtenemos una ip del isp podemos enviar una REQUEST.

### REQUEST

Las request tienen VERBO que determina la operacion del request:

GET: pide algun resource al server. \
POST: Le pedimos al servidor que acepte algo que enviamos.
PUT: Update de algo en el servidor. \
DELETE: Elimina informacion o algun recurso en el servidor.


### Response

Respuesta a la request. Tiene la siguiente estructura:

* Status line: status code. (basicos)
    * 200 OK
    * 404 NOT FOUND
* Message body: requerimento del usuario.

#### Resources

Los recursos son los servicios que estas ofreciendo. 

tienen: 
* PATH: Ubicacion en el file system del servidor. 
* PARAMETERS: Parametros necesarios para servir el recurso.
* STATUS CODE: Codigo que avisa el estado de la request al cliente.
* USED FOR: Proposito del recurso.
* METHODO: Operacion del protocolo HTTP que va a operar el recurso.