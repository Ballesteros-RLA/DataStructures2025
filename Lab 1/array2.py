def store_inventory():
    inventory = ["Apples", "Bananas", "Cherries", "Dates"] 
    print("Initial Inventory:", inventory)
    
  
    inventory.append("Elderberries")
    print("Updated Inventory:", inventory)
    
   
    inventory.remove("Bananas")
    print("Inventory after Removal:", inventory)
    
    
    item = "Cherries"
    if item in inventory:
        print(f"{item} is available in inventory.")
    else:
        print(f"{item} is not available.")

store_inventory()
