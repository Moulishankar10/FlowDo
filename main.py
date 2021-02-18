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
    print("""
        \n******************************************** MAIN MENU ***********************************************\n
                                Press 1 for adding a New Order.

                                Press 2 for displaying the Revenue options.

                                Press 3 for displaying the Inventory options.

                                Press 9 for exit.
        \n******************************************************************************************************\n
    """)

# LIST OF KEYMAPS TO BE DISPLAYED IN ORDER OPTIONS
def orderOptionsVisualizer():
    print("""
        \n******************************************** ORDER MENU **********************************************\n
                                Press 1 for Adding a new product.

                                Press 2 for Removing a product.

                                Press 3 for Viewing the bill.

                                Press 4 to Modify your order.

                                Press 5 to Proceed your order.

                                Press 9 for exit.
        \n******************************************************************************************************\n
    """)

# LIST OF KEYMAPS TO BE DISPLAYED IN REVENUE OPTIONS
def revenueOptionsVisualizer():
    print("""
        \n******************************************* REVENUE MENU *********************************************\n
                Press 1 for viewing the Revenue Database.
                
                Press 2 for viewing a Month's Total Revenue.

                Press 3 for viewing the product which generated the Maximum Profit in a month.

                Press 4 for viewing the product which generated the Minimum Profit in a month.

                Press 5 for viewing the Revenue Trend Graph for a year.

                Press 9 for exit.
        \n******************************************************************************************************\n
    """)
    

# LIST OF KEYMAPS TO BE DISPLAYED IN INVENTORY OPTIONS
def inventoryOptionsVisualizer():
    print("""
        \n****************************************** INVENTORY MENU *********************************************\n
                                Press 1 for Viewing the Stock Inventory.

                                Press 2 for Adding a new product to your inventory.

                                Press 3 for Removing a product from your inventory.

                                Press 4 to Modify the properties of existing products.

                                Press 9 for exit.
        \n*******************************************************************************************************\n
    """)

# USED TO CHECK IF THE COLUMN FOR THE MONTH IS CREATED OR NOT
def revMonthChecker():
    today = datetime.now()
    frmt = today.strftime('%m-%Y')
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
            print("\nMaximum limit reached !")
        else:

            inv_data = pd.read_csv('data/inventory.csv')
            flag = 0
            for i in range(len(inv_data)):
                flag = 0
                if inv_data["Product_Name"][i]==ele.upper():
                    if qn.isnumeric() == True:
                        
                        if int(qn) <= inv_data["Available_Stock"][i]:

                            self.prod_name.append(ele.upper())
                            self.quantity.append(int(qn))
                            self.price.append(inv_data["Selling_Price"][i])

                            if self.front==None and self.rear==None:
                                self.front=self.rear=0
                            else:
                                self.rear += 1
                            print("\n>>>>>>>> Product is Added to the Order. <<<<<<<<\n")
                            break

                        else:
                            print("\n!! Sorry for the inconvenience... Your required product is Out of Stock !!")
                            break
                    else:
                        print("\n!! Invalid Amount of Quantity !!")
                        break
                else:
                    flag = 1
            if flag == 1:
                print("\n!! Unavailable Product or Invalid Product !!")

    # FUNCTION TO REMOVE A PRODUCT FROM THE BILL
    def remove(self,ele):
        if self.isEmpty():
            print("\n!!! No Products are selected for the Order - Couldn't do Remove operation !!!\n")
        else:
            if ele in self.prod_name:
                ind = self.prod_name.index(ele)
                del self.prod_name[ind]
                del self.quantity[ind]
                self.rear -= 1
                print("\n>>>>>>>> Product is Removed from the Order. <<<<<<<<\n")
            else:
                print("\n!!! The Specified Product is not in the Order !!!\n")

    # FUNCTION TO DISPLAY CONTENTS OF THE BILL
    def display(self):
        if self.isEmpty():
            print("\n!!!Sorry, It's an Empty Bill !!!\n")
        else:
            self.total_price = list(np.array(self.quantity)*np.array(self.price))
            
            form = {'Product Name':self.prod_name,'Quantity':self.quantity,'Cost(1)':self.price,'Total Cost':self.total_price}
            res = pd.DataFrame(form)
            res.index=list(range(1,len(self.prod_name)+1))
            print(res)
            print("\n=============================================================\n")
            print(f"Total Items           :  {len(self.prod_name)}")
            print(f"Total Quantities      :  {sum(self.quantity)}")
            print(f"Grand Total           :  Rs.{sum(self.total_price)}")
            print("\n=============================================================\n")

    # FUNCTION TO MODIFY A PRODUCT NAME OR QUANTITY IN THE BILL
    def modify(self,ele):
        if self.isEmpty():
            print("\n!!! No Products are selected for the Order - Couldn't modify anything !!!\n")
        else:
            if ele in self.prod_name:
                ind = self.prod_name.index(ele.upper())
                key = int(input("\n                 Press 0 to modify the product name ..... \n\n                 Press 1 to modify the quantity .....\n\nYour Option : "))
                if key == 0:
                    self.prod_name[ind] = input("\nEnter the new product name : ").upper()
                elif key == 1:
                    self.quantity[ind] = int(input("\nEnter the new amount of quantity : "))
                print("\n>>>>>>>> Updated the Order. <<<<<<<<\n")
            else:
                print("\n!!! The Specified Product is not in the Order !!!\n")
        
    # FUNCTION TO PERFORM THE POST PROCESSING ACTIVITIES ONCE THE BILL IS CONFIRMED
    def postProcessor(self):
        today = datetime.now()
        frmt = today.strftime('%m-%Y')
        inv_data = pd.read_csv('data/inventory.csv')
        rev_data = pd.read_csv("data/revenue.csv")

        for i in range(len(inv_data)):
            for j in range(len(self.prod_name)):
                if inv_data["Product_Name"][i] == self.prod_name[j]:
                    inv_data["Available_Stock"][i] -= self.quantity[j]
        inv_data.to_csv('data/inventory.csv', index=False)
        
        for i in range(len(rev_data)):
            for j in range(len(self.prod_name)):
                if rev_data["Product_Name"][i] == self.prod_name[j]:
                    rev_data[str(frmt)][i] += self.total_price[j]
        rev_data.to_csv('data/revenue.csv', index=False)

        print("\n\n\n -------- Updated the Inventory Data! -------- \n")

#INDIVIDUAL FUNCTIONS USED IN REVENUE SUB MENU
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# FUNCTION TO VIEW THE REVENUE DATABASE
def viewRevenue():
    rev_data = pd.read_csv('data/revenue.csv')
    print("\n------------------------------------------ REVENUE DATABASE --------------------------------------------\n\n",rev_data.to_string(index=False))

# FUNCTION TO DISPLAY THE REVENUE GENERATED BY THIS MONTH
def viewMonthRevenue():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = input("\nEnter the time period (MM-YYYY) : ")
    if frmt[:2] in ['01','02','03','04','05','06','07','08','09','10','11','12'] and frmt in rev_data.columns:
        month_revenue = sum(list(rev_data[frmt]))
        print(f"\n                                    The revenue generated on {month[int(frmt[:2])-1]} {int(frmt[-4:])} -- Rs.{month_revenue}")
    else:
        print("\n!!!! Invalid Time Period or Non-Entried Time Period !!!!\n")

# FUNCTION TO DISPLAY THE MAXIMUM PROFIT GENERATED PRODUCTS 
def maxProfit():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = input("\nEnter the time period (MM-YYYY) : ")
    if frmt[:2] in ['01','02','03','04','05','06','07','08','09','10','11','12'] and frmt in rev_data.columns:
        max_amt = max(list(rev_data[frmt]))
        print(f"\n                     The following product(s) generated the maximum profit on {month[int(frmt[:2])-1]} {int(frmt[-4:])} : \n")
        for i in range(len(rev_data)):
            if rev_data[frmt][i] == max_amt:
                print("        * {}   -   Rs.{}".format(rev_data["Product_Name"][i],max_amt))
    else:
        print("\n!!!! Invalid Time Period or Non-Entried Time Period !!!!\n")

# FUNCTION TO DISPLAY THE MINIMUM PROFIT GENERATED PRODUCTS
def minProfit():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = input("\nEnter the time period (MM-YYYY) : ")
    if frmt[:2] in ['01','02','03','04','05','06','07','08','09','10','11','12'] and frmt in rev_data.columns:
        min_amt = min(list(rev_data[frmt]))
        print(f"\n                      The following product(s) generated the least profit on {month[int(frmt[:2])-1]} {int(frmt[-4:])} : \n")
        for i in range(len(rev_data)):
            if rev_data[frmt][i] == min_amt:
                print("        * {}   -   Rs.{}".format(rev_data["Product_Name"][i],min_amt))
    else:
        print("\n!!!! Invalid Time Period or Non-Entried Time Period !!!!\n")

# FUNCTION TO VISUALIZE THE REVENUE GENERATED BY MONTHS THROUGH A GRAPH        
def viewRevenueGraph():
    rev_data = pd.read_csv('data/revenue.csv')
    profits =[]
    months = []
    year = input("\nEnter the Year (YYYY) : ")
    for i in rev_data.columns:
        if year in i:
            rev_data = pd.read_csv("data/revenue.csv")
            cols = list(rev_data.columns)
            for i in cols:
                if i[-4:] == year:
                    months.append(month[int(i[:2])-1])
                    profits.append(sum(list(rev_data[i])))
            plt.scatter(months, profits,color ='red',linewidths=3) 
            plt.plot(months,profits,color="blue")
            plt.bar(months,profits,color="green",width = 0.2)
            plt.xlabel("Month") 
            plt.ylabel("Revenue Generated (INR)") 
            plt.title("Revenue for the year {}".format(year))  
            plt.show() 
            flag = 1
            break
        elif year not in i:
            flag = 0

    if flag == 0:
        print("\n!!!! Invalid Year or Non-Entried Year !!!!\n")
    

#INDIVIDUAL FUNCTIONS USED IN INVENTORY SUB MENU

# FUNCTION TO VIEW THE STOCK INVENTORY
def viewInventory():
    inv_data = pd.read_csv("data/inventory.csv")
    print("\n------------------------------------------ STOCK INVENTORY --------------------------------------------\n\n",inv_data.to_string(index=False))

# FUNCTION TO ADD A NEW PRODUCT TO THE INVENTORY
def addProdInventory():
    inv_data = pd.read_csv("data/inventory.csv")
    rev_data = pd.read_csv("data/revenue.csv")
    if len(inv_data) == 0:
        snum = 0
    else:
        snum = len(inv_data)
    snum += 1
    prod_code = input("\nEnter the Product Code : ").upper()
    prod_name = input("\nEnter the Product Name : ").upper()
    avail_stock = int(input("\nEnter the Available Stock : "))
    max_stock = int(input("\nEnter the Maximum Stock : "))
    cost_price = int(input("\nEnter the Cost Price : "))
    selling_price = int(input("\nEnter the Selling Price : "))
    inv_data.loc[len(inv_data.index)] = [snum,prod_code,prod_name,avail_stock,max_stock,cost_price,selling_price]
    inv_data.to_csv("data/inventory.csv",index=False)
    print("\n>>>>>>>> Product added to the Inventory. <<<<<<<<\n")

    temp_list = [0]*(len(rev_data.columns)-2)
    new_row = [prod_code,prod_name]
    rev_data.loc[len(rev_data.index)] = new_row + temp_list
    rev_data.to_csv("data/revenue.csv",index = False)
# FUNCTION TO REMOVE A PRODUCT FROM THE INVENTORY
def removeProdInventory():
    inv_data = pd.read_csv("data/inventory.csv")
    rev_data = pd.read_csv("data/revenue.csv")
    l = list(inv_data["Product_Name"])
    prod_name = input("\nEnter the product name to remove : ").upper()
    if prod_name in l:
        for i in range(len(inv_data)):
            if inv_data["Product_Name"][i] == prod_name:
                ind = i
        inv_data.drop([ind],axis = 0,inplace = True)
        inv_data.to_csv("data/inventory.csv",index = False)
        print("\n>>>>>>>> Product removed from the Inventory. <<<<<<<<\n")
    else:
        print("\n!!!! The Specified Product is not in the Inventory !!!!\n")

    for j in range(len(rev_data)):
        if rev_data["Product_Name"][j] == prod_name:
            ind = i
    rev_data.drop([ind],axis = 0,inplace = True)
    rev_data.to_csv("data/revenue.csv",index = False)
    
# FUNCTION TO MODIFY THE EXISTING VALUES OF A PRODUCT IN THE INVENTORY            
def modifyProduct():
    inv_data = pd.read_csv("data/inventory.csv")
    l = list(inv_data["Product_Name"])
    prod_name = input("\nEnter the product name to modify : ").upper()
    if prod_name in l:
        for i in range(len(inv_data)):
            if inv_data["Product_Name"][i] == prod_name:
                ind = i
        print("\n--------------------------------------------\n")
        print("\nPress 1 to modify Product Code.")
        print("\nPress 2 to modify Product Name.")
        print("\nPress 3 to modify Available Stock.")
        print("\nPress 4 to modify Maximum Stock")
        print("\nPress 5 to modify Cost Price.")
        print("\nPress 6 for modifying Selling Price.\n")
        print("\n--------------------------------------------\n")

        option = int(input("\nEnter your Option : "))
        if option == 1:
            inv_data["Product_Code"][ind] = input("\nEnter the new Product Code for this product : ")
        elif option == 2:
            inv_data["Product_Name"][ind] = input("\nEnter the new Product Name for this product : ").upper()
        elif option == 3:
            inv_data["Available_Stock"][ind] = int(input("\nEnter the new value for Available Stock : "))
        elif option == 4:
            inv_data["Maximum_Stock"][ind] = int(input("\nEnter the new value for Maximum Stock : "))
        elif option == 5:
            inv_data["Cost_Price"][ind] = int(input("\nEnter the new value for Cost Price : "))
        elif option == 6:
            inv_data["Selling_Price"][ind] = int(input("\nEnter the new value for Selling Pric e: "))
        elif option not in [1,2,3,4,5,6]:
                print("\n!!!!! Please enter the valid option !!!!!\n")

        inv_data.to_csv("data/inventory.csv",index=False)
        print("\n\n>>>>>>>> Updated the Inventory. <<<<<<<<\n")
    else:
        print("\n!!!! The Specified Product is not in the Inventory !!!!\n")


# FUNCTIONS FOR THE SUB MENU
# Order() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE CUSTOMER'S ORDER LIST TO PERFORM ALL THE ACTIONS.

def Order():
    l = int(input("\nEnter the number of products : "))
    b = Biller(l)
    now = datetime.now()

    def proceed():
            print("\n--------------------- YOUR FINAL BILL -----------------------\n")
            print(f"Bill Date : {now.strftime('%d-%m-%Y')}     Time : {now.strftime('%I:%M %p')}")
            print("\n-------------------------------------------------------------\n")
            b.display()
            print("\n\t   *** THANK YOU - HAVE A NICE DAY ***\n")
            print("\n-------------------------------------------------------------\n")
            proceed.key = input("\nDo you want to make any changes in the Order? (y/n) : ").lower()
            print("\n")
            
    
    while True:
        orderOptionsVisualizer()
        option = input("\nEnter your option : ")
        if option not in '123459':
            print("\n!!!!! Please enter the valid option !!!!!\n")
        else:
            order_opt = int(option)
            if order_opt == 1:
                if b.isFull():
                    print("\n\n!!! Maximum Limit Reached !!!\n")
                else:
                    ele = input("\nEnter the product name : ").upper()
                    qn = input("\nEnter the quantity : ")
                    b.enqueue(ele,qn)
                
            elif order_opt == 2:
                ele = input("\nEnter the product name : ").upper()
                b.remove(ele)
                
            elif order_opt == 3:
                if b.isEmpty():
                    print("\n!!! Sorry, It is an Empty Bill !!!\n")
                else:
                    print("\n------------------------- BILL ------------------------------\n")
                    print(f"Bill Date : {now.strftime('%d-%m-%Y')}     Time : {now.strftime('%I:%M %p')}")
                    print("\n-------------------------------------------------------------\n")
                    b.display()
            
            elif order_opt == 4:
                ele = input("\nEnter the product name : ").upper()
                b.modify(ele)
            
            elif order_opt == 5:
                if b.isEmpty():
                    print("\n!!! Couldn't proceed the Order - No Products are Selected !!!\n")
                else:
                    if len(b.quantity) != l:
                        print(f"\n\n!! You didn't ordered {l} number of products !!\n\n")
                        usr_res = input("Do you want to proceed the order (y/n) : ").lower()
                        print("\n")
                        if usr_res == 'y':
                            proceed()
                        elif usr_res == 'n':
                            continue    
                        else:
                            print("\n\n!!! Invalid Response !!!\n")
                            continue
                    else:
                        proceed()
                    
                    key = proceed.key
                    if key == "y":
                        continue
                    elif key == "n":
                        b.postProcessor()
                    else:
                        print("\n\n!!! Invalid Response !!!\n\n")
                        continue
                    print("\n\n                                |||||  Thanks for the Order |||||                \n")

            elif order_opt == 9:
                break
        
            
# Revenue() - A FUNCTION WHICH PROVIDES ANY KIND OF INFORMATION REGARDING THE OWNER'S REVENUE.            
def Revenue():
    # SUB FUNCTIONS SHOULD BE ADDED
    while True:
        revenueOptionsVisualizer()
        option = input("\nEnter your option : ")
        if option not in '12349':
            print("\n!!!!! Please enter the valid option !!!!!\n")
        else:
            rev_opt = int(option)
            if rev_opt == 1:
                viewRevenue()
            elif rev_opt == 2:
                viewMonthRevenue()
            elif rev_opt == 3:
                maxProfit()
            elif rev_opt == 4:
                minProfit()
            elif rev_opt == 5:
                viewRevenueGraph()
            elif rev_opt == 9:
                break
        
# Inventory() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE INVENTORY LIST TO PERFORM IT'S REALTED FUNCTIONS.
def Inventory():
    # SUB FUNCTIONS SHOULD BE ADDED
    while True:
        inventoryOptionsVisualizer()
        option = input("\nEnter your option : ")
        if option not in '12349':
            print("\n!!!!! Please enter the valid option !!!!!\n")
        else:
            inv_opt = int(option)
            if inv_opt == 1:
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
    \n======================================== WELCOME TO FLOWDO =========================================\n
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
        option = input("\nEnter your option : ")
        
        if option not in '1239':
            print("\n!!!!! Please enter the valid option !!!!!\n")
            
        else:
            opt = int(option)

            if opt == 1:
                Order()
                
            elif opt == 2:
                Revenue()
                
            elif opt == 3:
                Inventory()
                
            elif opt == 9:
                final_opt = input("\nDo you really want to exit FlowDo (y/n) : ").lower()
                if final_opt == "y":
                    print("\n\n\t\t\t\t\t  ~~~~~~ THANK YOU FOR USING FLOWDO ~~~~~~   \n\n")
                    break
                elif final_opt == 'n': 
                    continue   
                else:
                    print("\n\n\n\n!!!! Invalid Response !!!!\n")

            