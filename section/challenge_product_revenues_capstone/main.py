def calculate_revenue(prices, quantities_sold): 
    return [ prices[index]*quantities_sold[index] for index in range(len(prices))]
        
def formatted_output(revenues): 
    revenue_per_product = list(revenues)

    for revenue in revenue_per_product:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}") 

    
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = sorted(zip(products, revenue))

formatted_output(revenue_per_product)
# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")