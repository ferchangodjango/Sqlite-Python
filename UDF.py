import sqlite3
import pandas as pd

square=lambda n: n*n
try:
    with sqlite3.connect('E:/DB SQL3/DATA_BASE_NORTHWIND/Northwind.db') as comn:
        comn.create_function('Square',1,square)
        cursor=comn.cursor()
        cursor.execute("""
                    SELECT *,Square(Price)
                    FROM Products""")
        result=cursor.fetchall()
        results_DF=pd.DataFrame(result)
    
    print(results_DF)

except sqlite3.Error as e:
    print(f"Error en la base de datos: {e}")

finally:
    comn.close()
