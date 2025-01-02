# greetings = "Hello worid"
# print(greetings)

# Assign two numbers to variables a and b
# a = 10
# b = 5

# Calculate sum, difference, product, and quotient
# sum_result = a + b
# difference_result = a - b
# product_result = a * b
# quotient_result = a / b
#
# # Print the results
# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Quotient:", quotient_result)
#
#
# firstname = "Muneeb "
# lastname = "Ullah"
# # print(firstname + lastname)
#
# a:int = 5
# b:int = 10
#
# a ,b = a , b
# print("a =" , a)
# print("b =",b)
#
# # Create a variable count and set it to 0
# count = 0
#
# # Increment by 5, decrement by 2, and multiply by 3
# count += 5    # Increment by 5
# count -= 2    # Decrement by 2
# count *= 3    # Multiply by 3
#
# # Print the final value
# print(count)

# name = "Muneeb"
# age =24
# address = "Swabi"
# print(name,age,address)

# def myclass():
#     name = "muneeb"
#     age = 24
#     address = "swabi"
#     print(name,age,address)
# myclass()

# name = "muneeb"
# age = 24
# address = "swabi"
# profession = "student"
# def myfunc():
#     print(name,age,address,profession)
# myfunc()

# global variable
# x = 50  # Global variable
#
# def local_scope_example():
#     x = 20  # Local variable
#     print("Inside function, x is:", x)
#
# local_scope_example()  # Output: Inside function, x is: 20
# print("Outside function, x is:", x)  # Output: Outside function, x is: 50

# noinspection PyGlobalUndefined
# def replica():
#     global x
#     x = "Professional"
#     print(x)
# replica()
#
# def muneeb():
#    name = "muneeb"
#    age = 24
#    address = "swabi"
#    profession = "student"
#    print(name,age,address,profession)
# muneeb()

# x = "awesome"
#
#
# def myfunc():
#     global x
#
#
# x = "fantastic"
# print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
