import pandas as pd


class Vendor:
    def __init__(self, file_name, id_col, sp_col, stock_col):
        self.file_name = file_name
        self.df = pd.read_csv('data/' + file_name)
        self.id_col = id_col
        self.sp_col = sp_col
        self.stock_col = stock_col

    def change_values(self, n, input_id, input_sp, input_stock):
        for i in range(n):
            sku = self.df[self.df[self.id_col].str.contains(input_id[i])]
            if input_sp[i] != 'same':
                self.df.loc[sku.index, self.sp_col] = input_sp[i]
            for size, new_stock in zip(['S', 'M', 'L', 'XL', 'XXL'], input_stock[input_id[i]]):
                sku = self.df[self.df[self.id_col] == input_id[i] + '_' + size]
                if new_stock != 'same':
                    self.df.loc[sku.index, self.stock_col] = new_stock
        self.df.to_csv(self.file_name, index=False)  # make sure this is changed to save it in data
