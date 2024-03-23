import sqlite3
import pandas as pd

#Realizando conección con python
square=lambda n: n*n
try:
    with sqlite3.connect('E:/DB SQL3/DATA_BASE_NORTHWIND/Northwind.db') as comn:
        cursor=comn.cursor()
        cursor.execute("""
                    SELECT P.ProductID,P.ProductName,Price*Quantity AS Profit
                    FROM OrderDetails AS OD
                    INNER JOIN Products AS P ON OD.ProductID=P.ProductID
                    GROUP BY OD.ProductID
                    ORDER BY Profit DESC
                    LIMIT 10"""
                       )
        result=cursor.fetchall()
        results_DF=pd.DataFrame(result)
    
    with sqlite3.connect('E:/DB SQL3/DATA_BASE_NORTHWIND/Northwind.db') as comn2:
        cursor2=comn2.cursor()
        cursor2.execute("""
                        SELECT Employees.FirstName|| " " || Employees.LastName AS FullName,Products.Price,OrderDetails.Quantity,Products.Price*OrderDetails.Quantity AS TotalProfit
                        FROM OrderDetails 
                        INNER JOIN Orders ON Orders.OrderID=OrderDetails.OrderID
                        INNER JOIN Products ON OrderDetails.ProductID=Products.ProductID
                        INNER JOIN Employees ON Employees.EmployeeID=Orders.EmployeeID
                        GROUP BY FullName 
                        ORDER BY TotalProfit DESC
                        """
                       )
        result2=cursor2.fetchall()
        results2_DF=pd.DataFrame(result2)
    #print(results_DF)

except sqlite3.Error as e:
    print(f"Error en la base de datos: {e}")

finally:
    comn.close()
    comn2.close()


print(results_DF)