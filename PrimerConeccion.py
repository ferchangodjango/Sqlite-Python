#Importando librerias
import sqlite3
import pandas as pd
from bokeh.io import output_notebook,show
from bokeh.plotting import figure
from bokeh.layouts import layout

#Create the conection with Sqlite 3
conection_northwind=sqlite3.connect('E:/DB SQL3/DATA_BASE_NORTHWIND/Northwind.db')
query_top_seller='''
    SELECT Employees.FirstName|| " " || Employees.LastName AS FullName,Products.Price,OrderDetails.Quantity,Products.Price*OrderDetails.Quantity AS TotalProfit
    FROM OrderDetails 
    INNER JOIN Orders ON Orders.OrderID=OrderDetails.OrderID
    INNER JOIN Products ON OrderDetails.ProductID=Products.ProductID
    INNER JOIN Employees ON Employees.EmployeeID=Orders.EmployeeID
    GROUP BY FullName 
    ORDER BY TotalProfit DESC'''

TopSeller=pd.read_sql_query(query_top_seller,conection_northwind)

query_top_products='''
   SELECT P.ProductID,P.ProductName,Price*Quantity AS Profit
   FROM OrderDetails AS OD
   INNER JOIN Products AS P ON OD.ProductID=P.ProductID
   GROUP BY OD.ProductID
   ORDER BY Profit DESC
   LIMIT 10'''

Top_products=pd.read_sql_query(query_top_products,conection_northwind)

#Put contiditions for the colors
TopSellerBetterThanAvg=TopSeller.loc[TopSeller.TotalProfit>=TopSeller.TotalProfit.mean()]
TopSellerLessThanAvg=TopSeller.loc[TopSeller.TotalProfit<TopSeller.TotalProfit.mean()]

TopProductsThanAvg=Top_products.loc[Top_products.Profit>=Top_products.Profit.mean()]
TopProductsLessAvg=Top_products.loc[Top_products.Profit<Top_products.Profit.mean()]

#Making the graphs with Bokeh library
figure_1=figure(x_range=TopSeller.FullName,title='TOP_SELLER',plot_width=400,plot_height=400)
figure_1.xgrid.grid_line_color=None
figure_1.ygrid.grid_line_alpha=0.7
figure_1.xaxis.axis_label='Seller'
figure_1.yaxis.axis_label='Total Profit'
figure_1.y_range.start = 0
figure_1.xaxis.major_label_orientation = 1
figure_1.vbar(TopSellerBetterThanAvg.FullName,top=TopSellerBetterThanAvg.TotalProfit,color='#008000',width=0.9)
figure_1.vbar(TopSellerLessThanAvg.FullName,top=TopSellerLessThanAvg.TotalProfit,color='#E74C3C',width=0.9)

figure_2=figure(x_range=Top_products.ProductName,title='TOP_PRODUCTS',plot_width=400,plot_height=400)
figure_2.xgrid.grid_line_color=None
figure_2.ygrid.grid_line_alpha=0.7
figure_2.xaxis.axis_label='Products'
figure_2.yaxis.axis_label='Profit'
figure_2.y_range.start = 0
figure_2.xaxis.major_label_orientation = 1
figure_2.vbar(TopProductsThanAvg.ProductName,top=TopProductsThanAvg.Profit,color='#008000',width=0.9)
figure_2.vbar(TopProductsLessAvg.ProductName,top=TopProductsLessAvg.Profit,color='#E74C3C',width=0.9)

Lay_Out_Productos=layout([[figure_1],[figure_2]])
Lay_Out_Productos

show(Lay_Out_Productos)