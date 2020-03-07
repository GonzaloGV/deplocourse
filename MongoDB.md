# MongoDB

* MongoDB es una <b />base de datos basada en codumnetos</b>
, esto quiere decir que trabaja con una coleccion de documentos.

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
 




