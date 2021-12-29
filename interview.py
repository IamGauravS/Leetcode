import pandas as pd
import numpy as np 
data = {'trnx_id': [1085405, 1085404, 1085403, 1085402, 1085401, 1085400],
        'revenue': [185.55, 1345, 1078, 49.9, 2498, 1197],
        'price': ['39.95, 10.95', '269', '379, 699', '24.95', '1499, 999', '399'],
        'qty': ['3|6', '5', '1|1', '2', '1|1', '3'],
        'product': ['A,B', 'C', 'D,E', 'F', 'G,H', 'I']}

df = pd.DataFrame.from_dict(data)

print(df.head())

def convert_price(row):
    price = row['price']
    qty = row['qty']
    product = row["product"]
    column_names = ["trnx_id", "revenue", 'price', 'qty', 'product']

    prices = price.split(",")
    qtys = qty.split("|")
    products  = product.split(",")


    output_arr = []
    for i in range(len(prices)):
        temp_arr = []
        temp_arr.append(row["trnx_id"])
        temp_arr.append("revenue")
        temp_arr.append(prices[i])
        temp_arr.append(qty[i])
        temp_arr.append(products[i])
        output_arr.append(temp_arr)



    return pd.Series(output_arr, index = column_names) 


df_new = df.apply(convert_price, axis=1)