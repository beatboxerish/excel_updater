from Vendor import Vendor


def update_syntax(file, id_col, sp_col, stock_col, input_id, input_sp, input_stock):
    print('Updating for:', file)
    vendor = Vendor(file, id_col, sp_col, stock_col)
    vendor.change_values(n, input_id, input_sp, input_stock)
    print("Updating finished")
    print("---*---")


input_id = []
input_sp = []
temp_stock = []
input_stock = {}
print("Please enter number of designs to update:")
n = int(input())
for i in range(n):
    print("Please enter ID without size:")
    input_id.append(input())
    print("Please enter new Selling Price. Enter 'same' if you don't want to change it:")
    input_sp.append(float(input()))
    for size in ['S', 'M', 'L', 'XL', 'XXL']:
        print("Please enter current stock for size:", size, ". Enter 'same' if you don't want to change it:")
        temp_stock.append(int(input()))
    input_stock[input_id[-1]] = temp_stock

# flipkart
update_syntax('flipkart.csv', 'Seller SKU Id', 'Your Selling Price', 'System Stock count', input_id, input_sp,
              input_stock)

# 1566
update_syntax('1566.csv', 'SKU ID', 'Selling Price', 'Inventory', input_id, input_sp,
              input_stock)

# # 4460_aws
update_syntax('4460_aws.csv', 'SKU ID', 'MRP', 'QUANTITY', input_id, input_sp,
              input_stock)

# catalog_v2
update_syntax('catalog_v2.csv', 'Merchant SKU', 'Price', 'Quantity', input_id, input_sp,
              input_stock)
