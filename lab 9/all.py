

"""
week 11lab INFS1201
"""
def view(m):
    for (i,j) in m.items():
        print(f"{i:<10}     {j}")
def delete(m):
    item = input("which item would you like to remove: ")
    if item in m.keys():
        m.pop(item)
    else:
        print(f"{item} doesn't exit in the menu.")
def update(m):
    item = input("What item would you like to update? ")
    if item not in m.keys():
        print(f"{item} doesn't exist in the menu, how th will you update it?")
        ad = input("enter y if you want to add the item ")
        if ad.lower() == 'y':
            price = int(input(f"Enter the price for {item}"))
            m[item] = price
    else:
        price = int(input(f"Enter the new price for {item}: "))
        m[item] = price

def add(m):
    item = input("What item would you like to add? ")
    if item not in m.keys():
        price = int(input(f"What is the price of {item}"))
        m[item] = price
    else:
        print(f"{item} already exists in the menu")
def ex1():
    menuDict = {
        'soup':12,'salad':15,
        'hummus':10,'fattoush':13,
        'kebbeh':52,'pizza':19,'burger':22,
        'fries':12,'brownie':21
    }

    while True:
        print("Welcome to restaurant management system")
        print("1: view menu\n2: add new item\n3: update existing item\n4: delete item\n0: exit")

        option = input("Which operations do you want to perform (0 to 4)? ")
        while not option.isnumeric() and 0 <int(option)<4:
            print("Invalid option, try again")
            option = input("Which operations do you want to perform (0 to 4)? ")
        option = int(option)
        if option == 1:
            view(menuDict)
        elif option == 2:
            add(menuDict)
        elif option ==3:
            update(menuDict)
        elif option == 4:
            delete(menuDict)
        else:
            break
import random
def ex2():
    num = random.randint(65,122)
    while not(90>num>97):
        num= random.randint(65,122)
    print(chr(num))

def ex3(a,t):
    counter = 0
    if len(a) != len(t) and type(a) != type(t):
        print("Invalid , try again")
    for i in range(len(t)):
        if a[i] == t[i]:
            counter+=1
    print(counter)
print("hello1")
ex3('fs f','tsf')
print("hello?")