# Excel Files Updater and Uploader

This is a small project that I am working on for my brother. He has several online vendors selling his products. So he wanted a program that could update the stocks and selling price for all the vendors.
He gave me the excel sheets that would be used to maintain the inventory, selling price etc for the different vendors. 

This program accepts the number of designs, selling price and current stock as input from the user to create new and updated csv files that can be uploaded to the vendor's site.

### Files/Folders:
* data: contains all the original csv files
* output: contains all the updated csv files
* Vendor.py: contains the code for the Vendor class which is used to update
* main.py: the main program that the user must run
* rough.py: some very rough code that I used to clean up files, make initial draft etc. Not required 
now

### Libraries required:
1. pandas
2. xlrd
