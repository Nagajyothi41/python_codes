# 1. Grocery Store Programs
# Program 1: Grocery Bill Calculation
# Question: Write a Python program to accept the names, quantities, and prices of five grocery items. Calculate and display the total bill amount.
# Code:
# total = 0for i in range(5):    name = input("Enter item name: ")    quantity = int(input("Enter quantity: "))    price = float(input("Enter price per item: "))    cost = quantity * price    total = total + cost    print(name, "cost:", cost)print("Total bill: ₹", total)



# Output:
# Enter item name: Rice
# Enter quantity: 2
# Enter price per item: 60
# Rice cost: 120.0
# Enter item name: Sugar
# Enter quantity: 1
# Enter price per item: 45
# Sugar cost: 45.0
# Enter item name: Oil
# Enter quantity: 2
# Enter price per item: 150
# Oil cost: 300.0
# Enter item name: Milk
# Enter quantity: 2
# Enter price per item: 30
# Milk cost: 60.0
# Enter item name: Soap
# Enter quantity: 1
# Enter price per item: 35
# Soap cost: 35.0
# Total bill: ₹ 560.0


# Program 2: Grocery Discount Calculation
# Question: Write a Python program to apply a 10% discount if the total purchase amount exceeds ₹2,000. Display the original bill, discount, and final bill.
# Code:
# total = float(input("Enter total grocery bill: "))if total > 2000:    discount = total * 10 / 100else:    discount = 0final_bill = total - discountprint("Original bill: ₹", total)print("Discount: ₹", discount)print("Final bill: ₹", final_bill)



# Output:
# Enter total grocery bill: 2500
# Original bill: ₹ 2500.0
# Discount: ₹ 250.0
# Final bill: ₹ 2250.0


# Program 3: Stock Availability
# Question: Write a Python program to check whether sufficient stock is available for a customer's requested quantity.
# Code:
# item = input("Enter item name: ")stock = int(input("Enter available stock: "))required = int(input("Enter required quantity: "))if required <= stock:    print("Stock available")    print("Remaining stock:", stock - required)else:    print("Insufficient stock")    print("Available stock:", stock)



# Output:
# Enter item name: Rice
# Enter available stock: 50
# Enter required quantity: 20
# Stock available
# Remaining stock: 30


# Program 4: Daily Sales Analysis
# Question: Write a Python program to accept sales amounts for seven customers using a loop. Calculate total sales, average bill, and highest bill.
# Code:
# total = 0highest = 0for i in range(7):    bill = float(input("Enter customer bill: "))    total = total + bill    if bill > highest:        highest = billaverage = total / 7print("Total sales: ₹", total)print("Average bill: ₹", round(average, 2))print("Highest bill: ₹", highest)



# Output:
# Enter customer bill: 100
# Enter customer bill: 250
# Enter customer bill: 500
# Enter customer bill: 150
# Enter customer bill: 300
# Enter customer bill: 200
# Enter customer bill: 400
# Total sales: ₹ 1900.0
# Average bill: ₹ 271.43
# Highest bill: ₹ 500.0


# Program 5: Grocery Price Calculator Using Functions
# Question: Write a Python program using a function that accepts price and quantity. Apply a 5% discount if the quantity exceeds 10 units.
# Code:
# def calculate_cost(price, quantity):    total = price * quantity    if quantity > 10:        discount = total * 5 / 100    else:        discount = 0    return total - discountprice = float(input("Enter item price: "))quantity = int(input("Enter quantity: "))amount = calculate_cost(price, quantity)print("Final amount payable: ₹", amount)



# Output:
# Enter item price: 100
# Enter quantity: 12
# Final amount payable: ₹ 1140.0



# 2. Gold and Silver Store Programs
# Program 6: Gold Jewellery Bill Calculation
# Question: Write a Python program to accept gold weight, price per gram, and making charges. Calculate the total jewellery cost.
# Code:
# weight = float(input("Enter gold weight in grams: "))price = float(input("Enter gold price per gram: "))making = float(input("Enter making charges: "))gold_cost = weight * pricetotal = gold_cost + makingprint("Gold cost: ₹", gold_cost)print("Making charges: ₹", making)print("Total jewellery cost: ₹", total)



# Output:
# Enter gold weight in grams: 10
# Enter gold price per gram: 7000
# Enter making charges: 5000
# Gold cost: ₹ 70000.0
# Making charges: ₹ 5000.0
# Total jewellery cost: ₹ 75000.0


# Program 7: Gold Purchase Discount
# Question: Apply a 5% discount on making charges if the gold weight exceeds 20 grams.
# Code:
# weight = float(input("Enter gold weight: "))price = float(input("Enter gold price per gram: "))making = float(input("Enter making charges: "))gold_cost = weight * priceoriginal = gold_cost + makingif weight > 20:    discount = making * 5 / 100else:    discount = 0final_bill = original - discountprint("Original amount: ₹", original)print("Discount: ₹", discount)print("Final bill: ₹", final_bill)



# Output:
# Enter gold weight: 25
# Enter gold price per gram: 7000
# Enter making charges: 10000
# Original amount: ₹ 185000.0
# Discount: ₹ 500.0
# Final bill: ₹ 184500.0


# Program 8: Gold and Silver Price Comparison
# Question: Calculate gold and silver purchase costs and display which metal has the higher purchase cost.
# Code:
# gold_price = float(input("Enter gold price per gram: "))silver_price = float(input("Enter silver price per gram: "))gold_weight = float(input("Enter gold weight: "))silver_weight = float(input("Enter silver weight: "))gold_cost = gold_price * gold_weightsilver_cost = silver_price * silver_weightprint("Gold cost: ₹", gold_cost)print("Silver cost: ₹", silver_cost)if gold_cost > silver_cost:    print("Gold has the higher purchase cost")elif silver_cost > gold_cost:    print("Silver has the higher purchase cost")else:    print("Both costs are equal")



# Output:
# Enter gold price per gram: 7000
# Enter silver price per gram: 100
# Enter gold weight: 10
# Enter silver weight: 500
# Gold cost: ₹ 70000.0
# Silver cost: ₹ 50000.0
# Gold has the higher purchase cost


# Program 9: Daily Gold and Silver Sales Analysis
# Question: Accept gold and silver jewellery sales for seven days. Calculate total weekly sales, average daily sales, and highest daily sales.
# Code:
# total = 0highest = 0for day in range(1, 8):    gold = float(input("Enter gold sales: "))    silver = float(input("Enter silver sales: "))    daily = gold + silver    total = total + daily    if daily > highest:        highest = dailyaverage = total / 7print("Total weekly sales: ₹", total)print("Average daily sales: ₹", round(average, 2))print("Highest daily sales: ₹", highest)



# Output:
# Enter gold sales: 10000
# Enter silver sales: 2000
# Enter gold sales: 15000
# Enter silver sales: 3000
# Enter gold sales: 20000
# Enter silver sales: 5000
# Enter gold sales: 12000
# Enter silver sales: 4000
# Enter gold sales: 30000
# Enter silver sales: 5000
# Enter gold sales: 18000
# Enter silver sales: 2000
# Enter gold sales: 25000
# Enter silver sales: 4000
# Total weekly sales: ₹ 155000.0
# Average daily sales: ₹ 22142.86
# Highest daily sales: ₹ 35000.0


# Program 10: Jewellery Billing Using Functions
# Question: Create a function that accepts metal type, weight, and price per gram. Apply a 3% discount if the purchase amount exceeds ₹50,000.
# Code:.
# def calculate_bill(metal, weight, price):    total = weight * price    if total > 50000:        discount = total * 3 / 100    else:        discount = 0    final_bill = total - discount    print("Metal type:", metal)    print("Original amount: ₹", total)    print("Discount: ₹", discount)    print("Final bill: ₹", final_bill)metal = input("Enter metal type: ")weight = float(input("Enter weight in grams: "))price = float(input("Enter price per gram: "))calculate_bill(metal, weight, price)



# Output:
# Enter metal type: gold
# Enter weight in grams: 10
# Enter price per gram: 7000
# Metal type: gold
# Original amount: ₹ 70000.0
# Discount: ₹ 2100.0
# Final bill: ₹ 67900.0

print("a")