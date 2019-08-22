import pandas as pd


class Vendor:
    def __init__(self, file_name, id_col, sp_col, stock_col):
        """
        Creates a new object and defines some of it's attributes that will be used in the next function.
        :param file_name: file name
        :param id_col: column name for SKU ID column
        :param sp_col: column name for Selling Price column
        :param stock_col: column name for Inventory column
        """
        self.file_name = file_name
        self.df = pd.read_csv('data/' + file_name)
        self.id_col = id_col
        self.sp_col = sp_col
        self.stock_col = stock_col

    def change_values(self, n, input_id, input_sp, input_stock):
        '''
        Updates the values(Selling prices and new current stock) for different designs and different sizes.
        :param n: number of designs
        :param input_id: list of SKU IDs that need to be updated
        :param input_sp: list of selling prices
        :param input_stock: dictionary that maps SKU ID to a list stock available for different sizes
        '''
        for i in range(n):
            sku = self.df[self.df[self.id_col].str.contains(input_id[i])]
            if input_sp[i] != 'same':
                self.df.loc[sku.index, self.sp_col] = input_sp[i]
            for size, new_stock in zip(['S', 'M', 'L', 'XL', 'XXL'], input_stock[input_id[i]]):
                sku = self.df[self.df[self.id_col] == input_id[i] + '_' + size]
                if new_stock != 'same':
                    self.df.loc[sku.index, self.stock_col] = new_stock
        self.df.to_csv('output/' + self.file_name, index=False)
