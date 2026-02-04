# print("hello")
#     print("hello")

#ERROR identation
# A block is a group of statement that share the same indentation level and are executed as a single unit under a controlling statement
# In Python block stars after statement that ends with : 


# Python's input() function is used to take user input. By default, it returns the user input in form of string
# i.e input() user se data input leta hai or data ko variable mai string ke form mai assign karta hai by default

# x=input()
# hota kya h phir below!
# user types -> 45
# x=="45"✅  x==45❎ (by default)
# print(x)
# print(type(x))
# -> 45
# -> <class 'str>'


# x = int(input("Enter number: "))

# valid inputs
# "10"      → 10
# "-5"      → -5
# "0"       → 0

# invalid inputs(error ayega)
# "10.5"    ❌
# "abc"     ❌
# "12a"     ❌


# x = float(input("Enter decimal: "))

# valid inputs
# "10"      → 10.0
# "10.5"    → 10.5
# "-3.14"   → -3.14

# invalid inputs
# "abc"     ❌
# "10,5"    ❌   (comma not allowed)


# split()->string(sirf string) ko separator ke base par tod kar list banata hai.

# x,y=input("enter the following numbers: ").split()
# print("first number: ",x)
# print("second number: ",y)

# lets understand the flow of above:
# pehle input() user se data lega
# 10 20

# input() return karega
# "10 20"(ek single string)

# Ab .split() 
# "10 20".split()

# So,
# ["10", "20"]

# x, y = ["10", "20"]
# x = "10"
# y = "20"
