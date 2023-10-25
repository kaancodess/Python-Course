numbers = [5,51,24,78,45]

result = sum(numbers)
result = sum(numbers,10) # sum of the list + 10

products = [
    {"product_name":"iphone13" , "price" : 5000},
    {"product_name":"iphone14" , "price" : 6000},
    {"product_name":"iphone15" , "price" : 7000},
    {"product_name":"iphone15pro" , "price" : 0},
]

# result = [product["price"] for product in products]
total_price = sum([product["price"] for product in products])
#average_price = total_price / len(products) 

number_of_products = len([product for product in products if product["price"] > 0]) # getting the products which is have a price

average_price = total_price / number_of_products

# print(int(average_price))

result = round(1.1)
result = round(10.5) # goes to 10 
result = round(2.3) # 2
result = round(2.7) # 3
result = round(1.4242,2) # getting the first 2 number digit after the main number
result = round(1.426242,4)

print(result)