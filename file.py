num1 = 42  #- variable declaration
num2 = 2.3  #- variable declaration
boolean = True  #- type check
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #print entire tuple
print(pizza_toppings[1]) #print pizza toppings list
pizza_toppings.append('Mushrooms') # append Mushrooms into pizza toppings list
print(person['name']) #print John
person['name'] = 'George' #assign value of George to name instead of John
person['eye_color'] = 'blue' #add value of blue to eye_color inside of the person dictionary
print(fruit[2]) #print banana

if num1 > 45: #conditional value check
    print("It's greater") #print nothing because 42 is not greater than 45
else:
    print("It's lower") #print It's lower

if len(string) < 5: #conditional type check
    print("It's a short word!") #print based on condition
elif len(string) > 15: # else if conditional type check
    print("It's a long word!") #print based on condition
else:
    print("Just right!") #print if neither of the other 2 previous conditions are met

for x in range(5): 
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)