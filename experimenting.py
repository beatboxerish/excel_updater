import pandas as pd
import os
#
# # 1.xlsx
# df_1 = pd.read_excel("data/1.xlsx")
# # dropping columns
# df_1.drop(0,axis=0, inplace=True)
# df_1.dropna(how='all', axis=1, inplace=True)

# flipkart
flipkart = pd.read_csv("flipkart.csv")  # make changes here to get into data folder
flipkart.drop(0, axis=0 , inplace=True)
flipkart.loc[:, 'System Stock count'] = flipkart.loc[:, 'System Stock count'].astype('int')
print("Please enter number of designs to update:")
n = int(input())
input_id = []
input_sp = []
input_stock = []
for i in range(n):
    print("Please enter ID without size:")
    input_id.append(input())
    print("Please enter SP:")
    input_sp.append(float(input()))

for i in range(n):
    sku = flipkart[flipkart['Seller SKU Id'].str.contains(input_id[i])]
    if input_sp[i] != 'same':
        flipkart.loc[sku.index, 'Your Selling Price'] = input_sp[i]
    for size in ['S', 'M', 'L', 'XL', 'XXL']:
        sku = flipkart[flipkart['Seller SKU Id'] == input_id[i] + '_' + size]
        print("Please enter current stock for size:", size)
        input_stock = int(input())
        flipkart.loc[sku.index, 'System Stock count'] = input_stock
flipkart.to_csv('flipkart.csv', index=False)  # make sure this is changed to save it in data
print("Done")


# converting all in data folder to csv format
for workbook in os.listdir('data/'):
    try:
        temp_df = pd.read_excel('data/'+workbook)
    except:
        print(workbook)
        continue
    temp_df.to_csv('data/'+workbook +'.csv')