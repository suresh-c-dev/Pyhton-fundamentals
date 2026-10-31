#Formated String function.
def greet(name):
    return f"Hello ,{name}!"

print(greet("Suresh"))
print(greet("Uday Surya"))

#sum function
def add(a,b):
    return a+b
print("Sum of 2 numbers: ",sum(10,20))
print("Sum of 2 numbers: ",sum(100,234))

#To find Even Function
def is_even(num):
    return num%2==0
print(is_even(10))
print(is_even(5))

#convertation from celsius to fahrenheit
def celsius_to_fahrenheit(c):
    f=c*9/5+32
    return f
print("fahrenheit value is: ",celsius_to_fahrenheit(100))
print("fahrenheit value is: ",celsius_to_fahrenheit(265))

# print Data type
def type_data(value):
    return type(value).__name__
print("Data Type is: ",type_data(10))
print("Data Type is: ",type_data("suresh"))
print("Data Type is: ",type_data(2.7))
print("Data Type is: ",type_data(True))
print("Data Type is: ",type_data([1,2]))
print("Data Type is: ",type_data({"suresh":21}))