# multiline strings

a = '''can i have multiline 
written this way 
in python language.'''
print(a)

# using square brackets to access elements

b = "Hello World"
print(b[1])

# Loop

for x in "banana":
    print(x)

x = 5
y = "Syed"
print(x)
print(y)


#  format string
quantityofitem = 5
itemnumber = 12345
priceofitem = 99.99
myorder = "I want {} pieces of item {} for {} pounds."
print(myorder.format(quantityofitem, itemnumber, priceofitem))

car = 1
Brand = "Toyota"
Model = "Camry"
detailsOfCar = "I need {} car of Brand {} and Model {}"
print(detailsOfCar.format(car, Brand, Model))

#  String Concatenation
x = "Monday is the first"
y = " day of the week"
z = x + y
print(z)

a = "QA Analyst should be proficient"
b = " in Automation Testing"
c = a + b
print(c)

#  String Upper Case

a = 'My name is Syed Haq'
print(a.upper())

b =  "MY NAME IS SYED HAQ"
print(b.lower())