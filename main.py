import pandas as pd

def mainOptionsVisualizer():
    print("**********************************************************************************************\n")
    print("Press 0 for viewing options again.")
    print("Press 1 for Adding a new order")
    print("Press 2 for viewing your revenue for this month.")
    print("Press 3 for viewing your inventory.")
    print("Press 9 for exit.")
    print("\n**********************************************************************************************")
    
def orderOptionsVisualizer():
    print("**********************************************************************************************\n")
    print("Press 0 for viewing options again.")
    print("Press 1 for Adding new product.")
    print("Press 2 for Removing a product.")
    print("Press 3 for viewing the bill.")
    print("Press 4 to modify your order.")
    print("Press 5 to proceed your order.")
    print("Press 9 for exit.")
    print("\n**********************************************************************************************")
    
def revenueOptionsVisualizer():
    print("**********************************************************************************************\n")
    print("Press 0 for viewing options again.")
    print("Press 1 for viewing this month's total revenue.")
    print("Press 2 for viewing the product which generated the most profit.")
    print("Press 3 for viewing the product which generated the least profit.")
    print("Press 4 for viewing the revenue graph.")
    print("Press 9 for exit.")  
    print("\n**********************************************************************************************")
    
def Order():
    orderOptionsVisualizer()
    while True:
        opt = int(input("Enter your option : "))
        if opt == 0:
            orderOptionsVisualiser()
            continue
        elif opt == 9:
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


if __name__ == "__main__":
    print("Its FlowDo! I can help you manage your business with ease...")
    print(" Here is the list of options available to you...")
    inv_table,prod_code,prod_name,avail_stock,max_stock,revenue = dataImporter()
    mainOptionsVisualizer()
    while 1:
        option = int(input("Enter your option :"))
        if option == 0:
            mainOptionsVisualizer()
            continue
        elif option == 1:
            Order()
            continue
        elif option == 2:
            Revenue()
            continue
        elif option == 3:
            Inventory()
            continue
        elif option == 9:
            break
