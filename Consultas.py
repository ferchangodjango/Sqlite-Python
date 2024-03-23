## Importando librerias para realizar las consultas
import sqlite3
import pandas as pd

#Creando la funcion (Lambda en este caso) para hacer la funcion 
cubic_function= lambda n : n*n*n

#Esta conectandose a la base de datos, en este caso atravez de una ruta
#Caso muy raro, debes investigar como se hace con URL, o pasword y contraseñas
com=sqlite3.connect('E:/DB SQL3/DATA_BASE_NORTHWIND/Northwind.db')

#Creando la función que se ejecutara en SQL
com.create_function("cubic_function",1,cubic_function)

#Creando el cursor para poder realizar una consulta a la base SQL
cursor=com.cursor()

cursor.execute(
    """
    SELECT *
    FROM Products
    """)

#
results=cursor.fetchall()
Primer_consulta=pd.DataFrame(results)
cursor.close()
com.close()
print(Primer_consulta)