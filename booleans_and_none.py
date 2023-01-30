# boolean - True or False
# a = True
# b = False
#
# print(a == b) # False
#
# print(a != b) # True
# print(a >= b) # True
# print(a >= True) # True
# print(b <= False) # True

# print(True and False) # False
# print(False and True) # False
# print(False or True) # True because True is an option

# Booleans are useful for quickly checking the state of something.
# The other ares booleans are really useful are in validating data types.

# Booleans with data types
#
# hi = "Hello world!"
#
# # comes out false because of alphabet
# print(hi.isalpha()) # False
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("!")) # True
# print(hi.startswith("H")) # True
# # all of this is case

# x = 0
# y = 10
# z = -15
# print(bool(x)) # 0 is always considered as false
# print(bool(y)) # comes out as true because it is not a zero, it is "Something"
# print(bool(z))

# None == Null in a lot of other languages
# is an object type
print(bool(None)) # False
x = None
print(x == False) # False
print(x == True) # False

# Checking if a variable is None

print(x == None) # direct comparison- more complex situation
print(x is None) # Best practice for checking if something 'is None'

print(type(x)) # <class 'NoneType'>





