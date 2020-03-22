# MongoDB

* MongoDB es una <b />base de datos basada en documentos</b>
, esto quiere decir que trabaja con  colecciones de documentos.

## MongoDB server:
* Es el servidor donde se alojan y sirven las distintas db de mongo.

## MongoDB:
* Es un conjunto de conjutos de <b />Mongo documents</b>.
Estos conjuntos de documentos no forzan ningun tipo de esquema. El unico requisito es que cada documento de un conjunto tenga alguna similitud o un proposito relacionado.

## Mongo Document:
* Es un <b />conjunto de KEY-VALUE PAIRS</b>, como un JSON.
Los documentos tienen un esquema dinamico, es decir que no tienen que tener el mismo conjunto de campos o estructura y que los campos en comun pueden tener distintos tipos de data.

| RDBMS         | MongoDB           |
|----------     |---------:         |
| Database      | Database          |
| Table         | Colleccion        |
| Filas         | Documentos        |
| Columna       | Field             |
| Table Join    | Embedded Documents|
| Primary Key   | Default Key dada  |

## Embedded Documents:
* Son documentos dentro del campo de otro documento. Similar a cuando un JSON tiene un JSON en uno de sus valores.

## MongoDB vs Relational DB:

 Relational DB              ||  MongoDB         |
 ----- |:---:|----:|
 |Tiene un esquema fijo  que describe las tablas  y sus relaciones|| No tiene un esquema determinado y no existe el concepto de relacion|

 ## Como crear y eliminar dbs?

### Como modelar data en mongo?

Cada coleccion tienen que estar relacionados o tener el mismo proposito!

1. Disenar "Schema" en base a los requerimientos del usuario:
2. Combinar varios documentos en uno solo si se usan juntos. Tratar de evitar los joins.
3. Duplicar la data porque el espacio de disco es barato en relacion al tiempo de computo.
4. Hacer joins cuando se escribe, no en la lectura.
5. Optimizar el esquema en funcion del uso mas frecuente.
6. Hacer agregaciones complejas en el esquema.
 
 ### Crear una base de datos en MongoDB:
 * <b />use DATABASE_NAME</b> se usa para crear una base de datos. El comando va a crear una nueva base de datos si no hay ninguna con ese nombre, de los contrario va devolver la db preexistente con ese nombre.

 ### Eliminar una db:
 * db.dropDatabase() eliminar la db actual.

 ## Como crear y eliminar colecciones en MongoDB?

### Crear una collecion:
 * para crear una db hay que usar el comando db.createCollection(name, Options):
   * name: Nombre de la coleccion.
   * Options (Opcional): Un documento que sirve para especificar configuraciones de la coleccion.

Sin embargo, la creación de colleciones se puede hacer directamente con la inserción de un documento con el comando db.collectionName.insert(documento).

### Eliminar una colecion:
* Para eliminar una coleccion tenemos que usar el comando
db.COLLECTION_NAME.drop()

## Como hacer Queries a una coleccion?
### Escribir una querie:
* para hacer queries se usa el metodo find(): \
  * db.COLLECTION_NAME.find() \
  Sin embargo esto nos devuelve los documentos en un formato poco practico para la lectura.
  * db.COLLECTION_NAME.find().pretty(). \
  Mejora mucho el formato.

En los parametros del metodo find podemos establecer condiciones para filtrar en la busqueda, por ejemplo: \
db.usuarios.find({"name": "Romina"})

### Dentro del filter podemos pasar filtros:
Los filtros van a determinar ciertas operaciones para filtrar documentros:
* Igualdad:
  * db.COLECTION_NAME.find({key:valor para filtrar})
* Menos que:
  * db.COLECTION_NAME.find({key:{$lt:valor}})
* Menos o igual que:
  * db.COLECTION_NAME.find({key:{$lte:valor}})
* Mayor que:
  * db.COLECTION_NAME.find({key:{$gt:valor}})
* Mayor o igual que:
  * db.COLECTION_NAME.find({key:{$gte:valor}})
* Distinto que:
  * db.COLECTION_NAME.find({key:{$ne:valor}})
* AND:
  * db.COLECTION_NAME.find({$and:[{key:{$lte:value}}, key:{$gte:value}]})
* OR:
  * db.COLECTION_NAME.find({$or:[{key:{$lte:value}}, key:{$gte:value}]})

### Proyecciones:
Al haccer una query, las proyecciones nos permiten traer solo los campos que necesitamos:
* Esto se hace con un parametro dentro del metodo find() que recibe un array de booleanos donde podemos determinar que campos queremos recibir.
* Ejemplo:
  * db.COLECTION_NAME.find({query}, {"key_1":1, _id:0})

### Limitar cantidad de Documentos en el resultado de la query:
Con el metodo limit() encadenado al metodo find, podemos limitar la cantidad de documentos en la respuesta:
* Sintaxis:
  * db.COLECTION_NAME.find().limit(NUMERO)

### Ordenar la respuesta:
Con el metodo sort() encadenado al metodo find podemos ordenar los documentos en base a algun campo:
* Sintaxis:
  * db.COLECTION_NAME.find().sort({KEY:1})
Si pasamos 1 se van a ordenar de forma ascendente.
Si pasamos -1 se va a ordenar de forma descendiente.

## Update de Documentos en MongoDB:
Los metodos mas utilizados para hacer updates en una db de mongo son update() y save().
### update():
* El metodo update cambia un valor en documentos existentes:
  * db.COLECTIOn_NAME.update(CRITERIO_DE_SELECION, UPDATED_DATA)

## Eliminar un Documento:
### remove():
* El metodo remove acepta dos parametros:
  * deletion criteria - (opcional) regla para determinar que elementos se van a eleminar.
  * justOne -(optional) Si es true, solo se va a eliminar un documento.
* Sintaxis:
  * db.COLECTION_NAME.remove(deletion_criteria)



 




