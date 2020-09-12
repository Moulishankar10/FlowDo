import pandas as pd

def mainOptionsVisualizer():
    print("Press 0 for viewing options again.")
    print("Press 1 for Adding a new order")
    print("Press 2 for viewing your revenue for this month.")
    print("Press 3 for viewing your inventory.")
    print("Press 9 for exit.")
    
    
def dataImporter():
    inventory = pd.DataFrame(pd.read_csv('data/inventory.csv'))
    inventory_items = inventory.Product_Name
    return inventory_items


if __name__ == "__main__":
    print("Its FlowDo! I can help you manage your business with ease...")
    print(" Here is the list of options available to you...")
    inventory_items = dataImporter()
