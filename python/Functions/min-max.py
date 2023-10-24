numbers = [1,3,5,7,8,9,18,86,97]

result = min(numbers) # printing 1 because its the smallest number in the numbers list
result = max(numbers) # printing 97 because its the biggest number in the numbers list

letters = ["a","b","c","d","e"]

result = min(letters) # printing a becuase its the first letter in the alphabet
result = max(letters) # printing e because in the letter list its the last one in alphabetical order


names = ["John","Max","Alexandra","Michael"]

result = min(names) # printing Alexandra because starts with A first letter of alphabet
result = max(names) # printing Michael becuase M is the last in alphabetical order

result = min([len(name) for name in names]) # printing 3 because the shortest name in the names list is "Max"   

result = max(names, key = lambda name:len(name)) # printing Alexandra because longest name in the names list

products = [
    {"product_name": "iphone14" , "price": "3000"},
    {"product_name": "iphone15" , "price": "4000"},
    {"product_name": "iphone15pro" , "price": "5000"}
]

result = min(products,key = lambda product: product["price"])["product_name"]  # getting the cheapiest model of the list 
result = max(products,key = lambda product: product["price"])["product_name"]  # getting the most expensive model of the list 



print(result)