# FLOWDO
# FlowDo is a application created for the purpose of managing business activities like Inventory Maintenance, Billing, Sales analysis and other business functions.

# Developed by: Moulishankar M R (@Moulishankar10) , Vigneshwar K R (@ToastCoder), Vishal Balaji Sivaraman (@The-SocialLion)
# Development Status: Under development

# REQUIRED MODULES
import pandas as pd
import csv
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
    print("Press 2 for viewing the product which generated the most profit.")
    print("Press 3 for viewing the product which generated the least profit.")
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

        self.prod_name.append(ele)
        self.quantity.append(qn)

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
            print("\n------- BILL -------")
            res = "\n".join("{}    {}".format(x, y) for x, y in zip(self.prod_name, self.quantity))
            print(res,"\n")

    def modify(self,ele):
        if self.isEmpty():
            print("Sorry! It is an empty bill.")
        else:
            ind = self.prod_name.index(ele)
            key = int(input("\nPress 0 for modifying the product name ..... \n Press 1 for modifying the quantity .....\n"))
            if key == 0:
                self.prod_name[ind] = input("\nEnter the new product name : ")
            elif key == 1:
                self.quantity[ind] = int(input("\nEnter the new amount of quantity : "))
    def postProcessor(self):
        r = csv.reader(open('data/inventory.csv'))
        inventory = list(r)
        print(len(inventory))
        for i in range(len(inventory)-1):
            for j in range(len(self.prod_name)):
                if inventory[i][2] == self.prod_name[j]:
                    print("inventory[i][2]= ",inventory[i][2])
                    print("inventory[i][3] before = ",inventory[i][3])
                    inventory[i][3] = int(inventory[i][3])-self.quantity[j]
                    print("inventory[i][3] after = ",inventory[i][3])
                    print("self.quantity[j]= ",self.quantity[j])
                    
        writer = csv.writer(open('data/inventory.csv', 'w'))
        writer.writerows(inventory)
        print("Inventory Updated ! ")

#INDIVIDUAL FUNCTIONS USED IN REVENUE SUB MENU
def viewMonthRevenue():
    pass
def maxProfit():
    pass
def minProfit():
    pass
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
    l = int(input("Enter the number of products:"))
    b = Biller(l)
    
    while True:
        orderOptionsVisualizer()
        order_option = int(input("Enter your option : "))
        if order_option == 0:
            orderOptionsVisualizer()

        elif order_option == 1:
            ele = input("Enter the product name : ")
            qn = int(input("Enter the quantity:"))
            b.enqueue(ele,qn)
            
        elif order_option == 2:
            ele = input("Enter the product name : ")
            b.remove(ele)
            
        elif order_option == 3:
            b.display()
        
        elif order_option == 4:
            ele = input("Enter the product name : ")
            b.modify(ele)
        
        elif order_option == 5:
            print("Here's your final bill")
            b.display()
            key = input("Do you want to make any changes?(Y/N)")
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
            continue
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
    #inv_table,prod_code,prod_name,avail_stock,max_stock,revenue = dataImporter()
    while True:
        mainOptionsVisualizer()
        option = int(input("Enter your option :"))
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
