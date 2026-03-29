# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"
discount = 0

if(product_type == "Perishable"):
    if(days_until_expiration <= 3 and stock_level > 50):
        discount = 30
    elif((days_until_expiration >= 4 and days_until_expiration <= 6) or stock_level > 50):
        discount = 20
    elif(days_until_expiration > 6 or stock_level > 50):
        discount = 10
    print(f"{discount}% discount applied.")
else:
    print("No discount available for non-perishable items.")