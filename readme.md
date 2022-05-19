# Actualizador de carpeta digital de precios desde excel
Este proyecto es una solución para una necesidad de mi papa relacionada a su trabajo. Usualmente el editaba imagenes de productos con sus respectivos precios cada vez que habia un cambio de precios.


## Requerimientos
    - El excel "data.xlsx" DEBE existir para cualquier operación.
    - El excel "precios_nuevos.xlsx" SOLO DEBE existir para correr el actualizador.
    - La info de los excels tiene que estar en la hoja "Hoja 1" o en la hoja "Sheet1".
    - Los archivos de excel tienen que estar en el mismo directorio que el actualizador.


## INSTRUCCIONES PARA EL ACTUALIZADOR:
- tener un archivo "data.xlsx" (un excel) con los siguientes campos:  
    -'codigoDeBarras'  
    -'nombre'  
    -'imagen'  
    -'xCoord'  
    -'yCoord'  

- tener un archivo "precios_nuevos.xlsx" con los siguientes campos:  
    -'codigoDeBarras'  
    -'nombre'  
    -'precioFinal'  

- correr actualizador (mezcla la base de datos con los precios nuevos, cambia el formato de todas las imagenes vanilla  y por ultimo les aplica los precios nuevos)  


## INSTRUCCIONES PARA LAS HERRAMIENTAS DE COORDENADAS:

Hay dos herramientas para las coordenadas de los precios en la imagen detalladas a continuación:
    - actualizar_coord_bd: Este programa se usa para, una vez creada la base de datos, setear las coordenadas de cada precio solo clickeando en el lugar deseado.   
    - coordenadas: En caso de tener que agregar una imagen nueva por motivo de algún producto nuevo:  
        1- Correr este programa.  
        2- Elegir la imagen.  
        3- Clickear en el lugar deseado y ver en consola las coordenadas.  
        4- Actualizar manualmente el archivo "data.xlsx" los campos "xCoord" y "yCoord" con las coordenadas deseadas.  
        5- Guardar el archivo.  

## --------- ENGLISH ---------
## Digital price lists updater from excel
This project is a solution to a need that my father has related to his work. Usually he used to edit manually each product's image with it's respective price every time that there was a price increase (nearly each month).

## Used By
This project is used by the following companies:
    - My dad.
## Requirements
    - Excel file "data.xlsx" MUST exist for any operation.
    - Excel file "precios_nuevos.xlsx" MUST exist ONLY to run "actualizador".
    - Excel's info MUST be either in sheet "Hoja 1" or "Sheet1".
    - Excel files MUST be in the same directory of the programs.
    - Instructions
