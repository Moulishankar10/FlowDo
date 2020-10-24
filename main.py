# FLOWDO
# FlowDo is an application created for the purpose of managing business activities like Inventory Maintenance, Billing, Sales analysis and other business functions.

# Developed by:

# Moulishankar M R (@Moulishankar10)
# Vigneshwar K R (@ToastCoder)

# REQUIRED MODULES
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# VISUALIZER FUNCTIONS:
# Used to display keymaps for main menu and every submenu

# LIST OF KEYMAPS TO BE DISPLAYED IN MAIN MENU
def mainOptionsVisualizer():
    print("\n*************************************** MAIN MENU ********************************************\n")
    print("Press 0 for viewing the options again.")
    print("Press 1 for Adding a new order")
    print("Press 2 for displaying the revenue options.")
    print("Press 3 for displaying the inventory options.")
    print("Press 9 for exit.")
    print("\n**********************************************************************************************\n")

# LIST OF KEYMAPS TO BE DISPLAYED IN ORDER OPTIONS
def orderOptionsVisualizer():
    print("\n************************************* ORDER MENU *********************************************\n")
    print("Press 0 for viewing the options again.")
    print("Press 1 for Adding a new product.")
    print("Press 2 for Removing a product.")
    print("Press 3 for viewing the bill.")
    print("Press 4 to modify your order.")
    print("Press 5 to proceed your order.")
    print("Press 9 for exit.")
    print("\n**********************************************************************************************\n")

# LIST OF KEYMAPS TO BE DISPLAYED IN REVENUE OPTIONS
def revenueOptionsVisualizer():
    print("\n************************************ REVENUE MENU ********************************************\n")
    print("Press 0 for viewing the options again.")
    print("Press 1 for viewing this month's total revenue.")
    print("Press 2 for viewing the product which generated the maximum profit this month.")
    print("Press 3 for viewing the product which generated the minimum profit this month.")
    print("Press 4 for viewing the revenue graph.")
    print("Press 9 for exit.")  
    print("\n**********************************************************************************************\n")

# LIST OF KEYMAPS TO BE DISPLAYED IN INVENTORY OPTIONS
def inventoryOptionsVisualizer():
    print("\n************************************* INVENTORY MENU *****************************************\n")
    print("Press 0 for viewing the options again.")
    print("Press 1 for viewing your inventory.")
    print("Press 2 for Adding a new product to your inventory.")
    print("Press 3 for Removing a product from your inventory.")
    print("Press 4 to modify the properties of existing products.")
    print("Press 9 for exit.")  
    print("\n**********************************************************************************************\n")

# USED TO CHECK IF THE COLUMN FOR THE MONTH IS CREATED OR NOT
def revMonthChecker():
    today = datetime.today()
    frmt = "{}-{}".format(today.month,today.year)
    rev_data = pd.read_csv('data/revenue.csv')
    header = list(rev_data.columns)
    x = [0]*len(rev_data)
    if frmt not in header:
        rev_data[frmt] = x
    rev_data.to_csv("data/revenue.csv", index = False)
    
# CLASS FOR BILLING OPERATIONS
class Biller:

    def __init__(self,l):
        self.prod_name=[]
        self.quantity=[]
        self.price=[]
        self.total_price=[]
        self.limit=l
        self.front=None
        self.rear=None
        
    def isFull(self):
        return self.rear==self.limit-1
            
    def isEmpty(self):
        return self.front==None

    # FUNCTION TO ADD A NEW PRODUCT TO THE BILL        
    def enqueue(self,ele,qn):
        if self.isFull():
            print("\nMaximum limit reached!")
        else:
            if self.front==None and self.rear==None:
                self.front=self.rear=0
            else:
                self.rear += 1
        inv_data = pd.read_csv('data/inventory.csv')
        flag = 0
        for i in range(len(inv_data)):
            flag = 0
            if inv_data["Product_Name"][i]==ele.upper():
                if qn<=inv_data["Available_Stock"][i]:
                    self.prod_name.append(ele.upper())
                    self.quantity.append(qn)
                    self.price.append(inv_data["Selling_Price"][i])
                    break
                else:
                    flag += 1
            else:
                flag += 1
        if flag != 0:
            print("\nSorry for the inconvenience! Your required product is either in Out of Stock or Not in our Stock.")

    # FUNCTION TO REMOVE A PRODUCT FROM THE BILL
    def remove(self,ele):
        if self.isEmpty():
            print("\nSorry! It is an empty bill.")
        else:
            ind = self.prod_name.index(ele)
            del self.prod_name[ind]
            del self.quantity[ind]
            self.rear -= 1

    # FUNCTION TO DISPLAY CONTENTS OF THE BILL
    def display(self):
        if self.isEmpty():
            print("\nSorry! It is an empty bill.")
        else:
            self.total_price = list(np.array(self.quantity)*np.array(self.price))
            
            form = {'Product Name':self.prod_name,'Quantity':self.quantity,'Cost(1)':self.price,'Total Cost':self.total_price}
            res = pd.DataFrame(form)
            res.index=list(range(1,len(self.prod_name)+1))
            print(res)
            print("\n=======================================================\n")
            print("Grand Total           :  Rs.",sum(self.total_price))
            print("\n=======================================================\n")

    # FUNCTION TO MODIFY A PRODUCT NAME OR QUANTITY IN THE BILL
    def modify(self,ele):
        if self.isEmpty():
            print("\nSorry! It is an empty bill.")
        else:
            ind = self.prod_name.index(ele.upper())
            key = int(input("\nPress 0 for modifying the product name ..... \nPress 1 for modifying the quantity .....\n\nYour Option : "))
            if key == 0:
                self.prod_name[ind] = input("\nEnter the new product name : ").upper()
            elif key == 1:
                self.quantity[ind] = int(input("\nEnter the new amount of quantity : "))

    # FUNCTION TO PERFORM THE POST PROCESSING ACTIVITIES ONCE THE BILL IS CONFIRMED
    def postProcessor(self):
        today = datetime.today()
        inv_data = pd.read_csv('data/inventory.csv')
        for i in range(len(inv_data)):
            for j in range(len(self.prod_name)):
                if inv_data["Product_Name"][i] == self.prod_name[j]:
                    inv_data["Available_Stock"][i] -= self.quantity[j]
        inv_data.to_csv('data/inventory.csv', index=False)

        rev_data = pd.read_csv("data/revenue.csv")
        for i in range(len(rev_data)):
            for j in range(len(self.prod_name)):
                if rev_data["Product_Name"][i] == self.prod_name[j]:
                    frmt = "{}-{}".format(today.month,today.year)
                    rev_data[str(frmt)][i]+=self.total_price[j]
        rev_data.to_csv('data/revenue.csv', index=False)
        print("\nData Updated ! ")

#INDIVIDUAL FUNCTIONS USED IN REVENUE SUB MENU

# FUNCTION TO DISPLAY THE REVENUE GENERATED BY THIS MONTH
def viewMonthRevenue():
    today = datetime.today()
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    month_revenue = sum(list(rev_data[frmt]))
    print("\nThe revenue generated by this month is Rs.",month_revenue)

# FUNCTION TO DISPLAY THE MAXIMUM PROFIT GENERATED PRODUCTS 
def maxProfit():
    today = datetime.today()
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    max_amt = max(list(rev_data[frmt]))
    print("\nThe following product(s) generated the maximum profit : \n")
    for i in range(len(rev_data)):
        if rev_data[frmt][i] == max_amt:
            print("{} - Rs.{}".format(rev_data["Product_Name"][i],max_amt))

# FUNCTION TO DISPLAY THE MINIMUM PROFIT GENERATED PRODUCTS
def minProfit():
    today = datetime.today()
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    min_amt = min(list(rev_data[frmt]))
    print("\nThe following product(s) generated the least profit : \n")
    for i in range(len(rev_data)):
        if rev_data[frmt][i]==min_amt:
            print("{} - Rs.{}".format(rev_data["Product_Name"][i],min_amt))
        
# FUNCTION TO VISUALIZE THE REVENUE GENERATED BY MONTHS THROUGH A GRAPH        
def viewRevenueGraph():
    profits =[]
    months = []
    today = datetime.today()
    rev_data = pd.read_csv("data/revenue.csv")
    cols = list(rev_data.columns)
    for i in cols:
        if i[-4:] == str(today.year):
            months.append(i)
    for i in months:
        profits.append(sum(list(rev_data[i])))
    plt.scatter(months, profits,color ='red',linewidths=3) 
    plt.plot(months,profits,color="blue")
    plt.bar(months,profits,color="green",width = 0.5)
    plt.xlabel("Month") 
    plt.ylabel("Revenue") 
    plt.title("Revenue for this year")  
    plt.show() 
    

#INDIVIDUAL FUNCTIONS USED IN INVENTORY SUB MENU

# FUNCTION TO VIEW THE STOCK INVENTORY
def viewInventory():
    inv_data = pd.read_csv("data/inventory.csv")
    print("\n----------------------------------- STOCK INVENTORY -----------------------------\n",inv_data)

# FUNCTION TO ADD A NEW PRODUCT TO THE INVENTORY
def addProdInventory():
    inv_data = pd.read_csv("data/inventory.csv")
    serial = int(input("\nEnter the Serial No : "))
    prod_code = input("\nEnter the Product Code : ")
    prod_name = input("\nEnter the Product Name : ")
    avail_stock = int(input("\nEnter the Available Stock : "))
    max_stock = int(input("\nEnter the Maximum Stock : "))
    cost_price = int(input("\nEnter the Cost Price : "))
    selling_price = int(input("\nEnter the Selling Price : "))
    inv_data.loc[len(inv_data.index)] = [serial,prod_code,prod_name,avail_stock,max_stock,cost_price,selling_price]
    inv_data.to_csv("data/inventory.csv",index=False)
    print("\nProduct Added to Inventory!")

# FUNCTION TO REMOVE A PRODUCT FROM THE INVENTORY
def removeProdInventory():
    ind = 0
    inv_data = pd.read_csv("data/inventory.csv")
    prod_name = input("Enter the product name to remove: ").upper()
    for i in range(len(inv_data)):
        if inv_data["Product_Name"][i] == prod_name:
            ind = i
    inv_data.drop([ind],axis = 0,inplace = True)
    inv_data.to_csv("data/inventory.csv",index=False)
    print("\nProduct is Removed from Inventory!")
            
# FUNCTION TO MODIFY THE EXISTING VALUES OF A PRODUCT IN THE INVENTORY            
def modifyProduct():
    ind = 0
    inv_data = pd.read_csv("data/inventory.csv")
    prod_name = input("Enter the product name to modify: ").upper()
    for i in range(len(inv_data)):
        if inv_data["Product_Name"][i] == prod_name:
            ind = i
    print("\nPress 1 to modify Product Code.")
    print("Press 2 to modify Product Name.")
    print("Press 3 to modify Available Stock.")
    print("Press 4 to modify Maximum Stock")
    print("Press 5 to modify Cost Price.")
    print("Press 6 for modifying Selling Price.")
    print("Press 9 for exit.\n")  
    option = int(input("Enter your Option: "))
    if option == 1:
        inv_data["Product_Code"][ind] = input("\nEnter the new Product Code for this product: ")
    elif option == 2:
        inv_data["Product_Name"][ind] = input("\nEnter the new Product Name for this product: ").upper()
    elif option == 3:
        inv_data["Available_Stock"][ind] = int(input("\nEnter the new value for Available Stock: "))
    elif option == 4:
        inv_data["Maximum_Stock"][ind] = int(input("\nEnter the new value for Maximum Stock: "))
    elif option == 5:
        inv_data["Cost_Price"][ind] = int(input("\nEnter the new value for Cost Price: "))
    elif option == 6:
        inv_data["Selling_Price"][ind] = int(input("\nEnter the new value for Selling Price: "))

    inv_data.to_csv("data/inventory.csv",index=False)
    print("\nModified the mentioned values!")

# FUNCTIONS FOR THE SUB MENU
# Order() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE CUSTOMER'S ORDER LIST TO PERFORM ALL THE ACTIONS.
def Order():
    l = int(input("\nEnter the number of products : "))
    b = Biller(l)
    
    while True:
        orderOptionsVisualizer()
        order_option = int(input("Enter your option : "))
        if order_option == 0:
            orderOptionsVisualizer()

        elif order_option == 1:
            ele = input("\nEnter the product name : ").upper()
            qn = int(input("\nEnter the quantity : "))
            b.enqueue(ele,qn)
            
        elif order_option == 2:
            ele = input("\nEnter the product name : ").upper()
            b.remove(ele)
            
        elif order_option == 3:
            print("\n----------------------- BILL --------------------------\n")
            b.display()
        
        elif order_option == 4:
            ele = input("\nEnter the product name : ").upper()
            b.modify(ele)
        
        elif order_option == 5:
            print("\n-------------------- YOUR FINAL BILL ------------------\n")
            b.display()
            print("---------------------------------------------------------\n")
            key = input("\nDo you want to make any changes? (Y/N) : ")
            if key == "Y" or key == "y":
                pass
            elif key == "N" or key == "n":
                b.postProcessor()
        elif order_option == 9:
            break
            
# Revenue() - A FUNCTION WHICH PROVIDES ANY KIND OF INFORMATION REGARDING THE OWNER'S REVENUE.            
def Revenue():
    # SUB FUNCTIONS SHOULD BE ADDED
    
    while True:
        revenueOptionsVisualizer()
        rev_opt = int(input("\nEnter your option : "))
        if rev_opt == 0:
            revenueOptionsVisualizer()
        if rev_opt == 1:
            viewMonthRevenue()
        if rev_opt == 2:
            maxProfit()
        if rev_opt == 3:
            minProfit()
        if rev_opt == 4:
            viewRevenueGraph()
        elif rev_opt == 9:
            break
        
# Inventory() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE INVENTORY LIST TO PERFORM IT'S REALTED FUNCTIONS.
def Inventory():
    # SUB FUNCTIONS SHOULD BE ADDED
    while True:
        inventoryOptionsVisualizer()
        inv_opt = int(input("\nEnter your option : "))
        if inv_opt == 0:
            inventoryOptionsVisualizer()
        elif inv_opt == 1:
            viewInventory()
        elif inv_opt == 2:
            addProdInventory()
        elif inv_opt == 3:
            removeProdInventory()
        elif inv_opt == 4:
            modifyProduct()
        elif inv_opt == 9:
            break
            
# MAIN FUNCTION
if __name__ == "__main__":
    
    print("""
    \n======================================= WELCOME TO FLOWDO =========================================\n
                             LET'S HAVE YOUR BUSINESS WITH EASE BY FLOWDO             
                        
              _______________________________________________________________________
             |                                                                       |
             |           FIRST, SETUP YOUR INVENTORY TO PROCEED THE ORDERS           |
             |                                                                       |
             |        ```````````````````````````````````````````````````````        |
             |                                                                       |
             |         IF IT IS ALL SET, PLEASE ENSURE THAT ALL THE PRODUCTS         |
             |                                                                       |
             |                 ARE IN SUFFICIENT QUANTITY TO PROCEED                 |
             |                                                                       |
             |                              THE ORDERS                               |
             |                                                                       |
             |        ```````````````````````````````````````````````````````        |
             |                                                                       |
             |                          NOW, LET'S MOVE ON!                          |
             |                                                                       |
             |_______________________________________________________________________|

    """)
    today = datetime.today()
    revMonthChecker()
    while True:
        mainOptionsVisualizer()
        option = int(input("\nEnter your option : "))
        if option == 0:
            mainOptionsVisualizer()
            
        elif option == 1:
            Order()
            
        elif option == 2:
            Revenue()
            
        elif option == 3:
            Inventory()
            
        elif option == 9:
            break
