from Vendor import Vendor


def update_syntax(file, id_col, sp_col, stock_col, input_id, input_sp, input_stock):
    '''
    Uses the Vendor class to create an object and then update the various values given the the input lists.
    :param file: file name (eg: flipkart.csv)
    :param id_col: column name for SKU ID column
    :param sp_col: column name for Selling Price column
    :param stock_col: column name for Inventory column
    :param input_id: list of SKU IDs that need to be updated
    :param input_sp: list of selling prices
    :param input_stock: dictionary that maps SKU ID to a list stock available for different sizes
    :return: nothing
    '''
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
    inp = input()
    if inp != 'same':
        inp = float(inp)
    input_sp.append(inp)
    for size in ['S', 'M', 'L', 'XL', 'XXL']:
        print("Please enter current stock for size:", size, ". Enter 'same' if you don't want to change it:")
        inp = input()
        if inp != 'same':
            temp_stock.append(int(inp))
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
