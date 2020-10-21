# FLOWDO
# FlowDo is a application created for the purpose of managing business activities like Inventory Maintenance, Billing, Sales analysis and other business functions.

# Developed by: Moulishankar M R (@Moulishankar10) , Vigneshwar K R (@ToastCoder), Vishal Balaji Sivaraman (@The-SocialLion)
# Development Status: Under development

# REQUIRED MODULES
import numpy as np
import pandas as pd
from datetime import datetime

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
            
    def enqueue(self,ele,qn):
        if self.isFull():
            print("Maximum limit reached!")
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
           

    def remove(self,ele):
        if self.isEmpty():
            print("Sorry! It is an empty bill.")
        else:
            ind = self.prod_name.index(ele)
            del self.prod_name[ind]
            del self.quantity[ind]
            self.rear -= 1
    
    def display(self):
        if self.isEmpty():
            print("Sorry! It is an empty bill.")
        else:
            self.total_price = list(np.array(self.quantity)*np.array(self.price))
            
            form = {'Product Name':self.prod_name,'Quantity':self.quantity,'Cost(1)':self.price,'Total Cost':self.total_price}
            res = pd.DataFrame(form)
            res.index=list(range(1,len(self.prod_name)+1))
            print(res)
            print("\n=======================================================\n")
            print("Grand Total           :  Rs.",sum(self.total_price))
            print("\n=======================================================\n")

    def modify(self,ele):
        if self.isEmpty():
            print("Sorry! It is an empty bill.")
        else:
            ind = self.prod_name.index(ele.upper())
            key = int(input("\nPress 0 for modifying the product name ..... \nPress 1 for modifying the quantity .....\nYour Option : "))
            if key == 0:
                self.prod_name[ind] = input("\nEnter the new product name : ").upper()
            elif key == 1:
                self.quantity[ind] = int(input("\nEnter the new amount of quantity : "))
    def postProcessor(self):
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
def viewMonthRevenue():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    month_revenue = sum(list(rev_data[frmt]))
    print("\nThe revenue generated by this month is Rs.",month_revenue)

def maxProfit():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    max_revenue = max(list(rev_data[frmt]))
    for i in range(len(rev_data)):
        if rev_data[frmt][i] == max_revenue:
            res = rev_data["Product_Name"][i]

    print(f"\n{res} has generated the maximum profit this month.")
def minProfit():
    rev_data = pd.read_csv('data/revenue.csv')
    frmt = "{}-{}".format(today.month,today.year)
    min_lt = list(rev_data[frmt])
    min_amount = min(min_lt)
    print("The following product(s) generated the least profit : ")
    if min_lt.count(min_amount) > 1:
        for i in range(len(rev_data)):
            

def viewRevenueGraph():
    pass

#INDIVIDUAL FUNCTIONS USED IN INVENTORY SUB MENU
def viewInventory():
    pass
def addProdInventory():
    pass
def removeProdInventory():
    pass
def modifyProduct():
    pass

# FUNCTIONS FOR THE SUB MENU

# Order() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE CUSTOMER'S ORDER LIST TO PERFORM ALL THE ACTIONS.
def Order():
    l = int(input("Enter the number of products : "))
    b = Biller(l)
    
    while True:
        orderOptionsVisualizer()
        order_option = int(input("Enter your option : "))
        if order_option == 0:
            orderOptionsVisualizer()

        elif order_option == 1:
            ele = input("Enter the product name : ").upper()
            qn = int(input("Enter the quantity : "))
            b.enqueue(ele,qn)
            
        elif order_option == 2:
            ele = input("Enter the product name : ").upper()
            b.remove(ele)
            
        elif order_option == 3:
            print("\n----------------------- BILL --------------------------\n")
            b.display()
        
        elif order_option == 4:
            ele = input("Enter the product name : ").upper()
            b.modify(ele)
        
        elif order_option == 5:
            print("\n-------------------- YOUR FINAL BILL ------------------\n")
            b.display()
            print("---------------------------------------------------------\n")
            key = input("Do you want to make any changes? (Y/N) : ")
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
        rev_opt = int(input("Enter your option : "))
        if rev_opt == 0:
            revenueOptionsVisualizer()
        if rev_opt == 1:
            viewMonthRevenue()
        if rev_opt == 2:
            maxProfit()
        if rev_opt == 3:
            minProfit()
        elif rev_opt == 9:
            break
        
# Inventory() - A FUNCTION WHICH PROVIDES THE ACCESSIBILITY TO THE INVENTORY LIST TO PERFORM IT'S REALTED FUNCTIONS.
def Inventory():
    # SUB FUNCTIONS SHOULD BE ADDED
    while True:
        inventoryOptionsVisualizer()
        inv_opt = int(input("Enter your option : "))
        if inv_opt == 0:
            inventoryOptionsVisualizer()
            continue
        elif inv_opt == 9:
            break
            
#def dataImporter():
#    inventory = pd.DataFrame(pd.read_csv('data/inventory.csv'))
#    revenue = pd.DataFrame(pd.read_csv('data/revenue.csv'))
   
#    inv_table = inventory
#    prod_code = inventory.Product_Code
#    prod_name = inventory.Product_Name
#    avail_stock = inventory.Available_Stock
#    max_stock = inventory.Maximum_Stock
#    return inv_table,prod_code,prod_name,avail_stock,max_stock,revenue



        
        

# MAIN FUNCTION
if __name__ == "__main__":
    print("Its FlowDo! I can help you manage your business with ease...")
    print(" Here is the list of options available to you...")
    today = datetime.today()
    #inv_table,prod_code,prod_name,avail_stock,max_stock,revenue = dataImporter()
    while True:
        mainOptionsVisualizer()
        option = int(input("Enter your option : "))
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
