import pandas as pd

def mainOptionsVisualizer():
    print("Press 0 for viewing options again.")
    print("Press 1 for Adding a new order")
    print("Press 2 for viewing your revenue for this month.")
    print("Press 3 for viewing your inventory.")
    print("Press 9 for exit.")
    
    
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
    while(1):
    option = int(input("Enter an option:"))
        if option == 0:
            mainOptionsVisualizer()
            break
        elif option == 1:
            newOrder(prod_name)
            break
        elif option == 2:
            Revenue(revenue)
            break
        elif option == 3:
            Inventory(inv_table)
            break
