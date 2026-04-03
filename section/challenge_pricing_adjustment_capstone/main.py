grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs = list(grocery_inventory["Eggs"])

if(eggs[1] > 5):
    print ("Eggs are too expensive, reducing the price by $1.")
    eggs[1] = eggs[1]-1
    grocery_inventory["Eggs"] = tuple(eggs)
else:
    print("The price of Eggs is reasonable")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)

print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk = list(grocery_inventory["Milk"])

if(milk[2] < 10):
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk[2] = milk[2] + 20
    grocery_inventory["Milk"] = tuple(milk)
else:
    print("Milk has sufficient stock")

apples = list(grocery_inventory["Apples"])

if(apples[1] > 2):
    print("Apples removed from inventory due to high price")
    grocery_inventory.pop("Apples")
    
print(f"Updated inventory: {grocery_inventory}")