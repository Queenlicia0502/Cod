# Assigning Different Variables
name = "penguin"
age  = 15
is_student = True
weight = 38.5

#Printing Different Variables and their Data Type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data  Type of Age is", type(age))

print("is_student :", is_student)
print("Data Type of weight is", type(is_student))

print("weight :", weight)
print("Data Type of weight is", type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Castsing....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of weight is", type(weight))