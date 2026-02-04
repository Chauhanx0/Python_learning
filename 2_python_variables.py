# What will be the output of the following code? Python
# x = "False" 
# y = bool(x) 
# print(y)

# let's understand 
# x = "False"
# Here, x is a string that literally contains the word "False". It's not the Boolean value False.

# y = bool(x) (matalab y mai abb boolean type ke basis pr store hogi value entered if empty-> store as false if non-empty-> store as true)
# Rules in Python for bool():
# Empty sequences/values (like "", 0, [], {}, None) → False
# Non-empty sequences/values → True

# Since "False" is a non-empty string, bool("False") will be:
# True
# print(y)
# True


# What is the result of the following code? Python 
# x = [1, 2, 3] 
# y = str(x) 
# print(y)

# x = [1, 2, 3] → creates a list with three integers: 1, 2, 3. ✅
# y = str(x) → converts the list x into a string. In Python, str([1, 2, 3]) becomes the string "[1, 2, 3]". Notice the quotes are not printed, they just mean y is of type str.
# print(y) → prints the string representation of the list: [1, 2, 3].

# x = "1.23" 
# y = complex(x) 
# print(y)
#(1.23+0j)-> output
