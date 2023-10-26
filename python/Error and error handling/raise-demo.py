# create a factorial functions which is given a error messages
# def factorial(x):
#     x = int(x)

#     if (x < 0):
#         raise ValueError("negative")

#     result = 1
#     for i in range(1, x+1):
#         result *= i

#     return result

# for i in [5,7,"a",2,-4,"10a",]:
#     try:
#         x = factorial(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# if there is a turkish letter in the password return error

def passwordControl(password):
    turkish_letters = "şçğüöıİ"

    for i in password:
        if i in turkish_letters:
            raise TypeError("password contains a turkish letter")
        
    print("valid password")

password = input("password: ")

try:
    passwordControl(password)

except TypeError as e:
    print(e)