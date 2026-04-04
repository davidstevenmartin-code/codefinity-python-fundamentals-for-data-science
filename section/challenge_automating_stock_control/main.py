# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    inventory_item = inventory[item]
    
    while(inventory_item[0] < inventory_item[1]):
        inventory_item[0] += inventory_item[2]
        
    if(inventory_item[1] > discount_threshold):
        inventory_item[3] = True
      
print("processing completed")