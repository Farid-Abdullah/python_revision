
"""
week 11lab INFS1201
"""

menuDict = {
        'soup':12,'salad':15,
        'hummus':10,'fattoush':13,
        'kebbeh':52,'pizza':19,'burger':22,
        'fries':12,'brownie':21
    }
grades = {     # tuples as keys that contain course code and course credit, score/100 as values
               # this dictionary is used for exercise 6 at line 144
    ('COMM1020',3):0,
    ('INFS1201',4):90,
    ('INFT1201',4):96,
    ('MATH1030',3):88
}

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
    '''Uses the above functions to view or modify the dictionary menuDict (line 7)'''
    #global menuDict # no need for this
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

def ex2():
    '''Takes order from the customer based on the "menuDict" dictionary that's in the main program line 7 '''
    order = dict() # will save all the ordered items in this dictionary
    item = input("What would you like to order? ")
    total = 0
    while True:
        if item in menuDict.keys():
            print(f"{item} is priced at {menuDict[item]}")
            num = input(f"How much {item} would you like to order? ")
            while not (num.isnumeric() and int(num)>0):
                print("enter a positive number please.")
                num = input(f"How much {item} would you like to order? ")
            num = int(num)
            order[item] = num
            total+= num*menuDict[item]
            more = input("Anything else? (y/n) : ")
            while more.lower() not in ('y','n'):
                    print("invalide choice, please enter 'y' or 'n' ")
                    more = input("Anything else? (y/n) : ")
            if more.lower() == 'n':
                break
            else:
                item = input("What else would you like to order? ")
            
                
        else:
            print(f"{item} is not in the menu, here's our menu:")
            view(menuDict)
            item = input("What would you like to order? ")
    print("Here's a summary of your order: ")
    for i,j in order.items():
        print(f"- {i} : {j}")
    print(f"Total bill: {total}QAR")

            
        

import random
def ex3():
    '''
    Just prints a random alphabet letter using ascii and chr() function
    '''
    num = random.randint(65,122)
    while not(90>num>97):
        num= random.randint(65,122)
    print(chr(num))

def ex4(a,t):
    '''takes two strings, return the number of matching characters
    for example ex4("TTFT","TTTT") will return 3'''
    counter = 0
    if len(a) != len(t) and type(a) != type(t):
        print("Invalid , try again")
    for i in range(len(t)):
        if a[i] == t[i]:
            counter+=1
    return counter
def ex5(menu):
    '''takes in dictionary that contains menu similar to menuDict in ex1, 
    return the most expensive dish and it's price'''
    max_price = max(menu.values())

    items = [i for i,j in menu.items() if j == max_price]
    
    if len(items)==1:
        print(f"The most expensive dish is {items[0]}")
    else:
        print(f"The most expensive dishes are :")
        for i in items: 
            print(i) 
        print(f"they cost {max_price} each")

def grade2gpa(grade):
    if grade>=90:
        return 4
    elif grade>=85:
        return 3.5
    elif grade>=80:
        return 3
    elif grade>=70:
        return 2.5
    elif grade>=60:
        return 2
    else:
        return 0
def ex6(g = grades.copy()): # = grades.copy() in case no arguments is passed, then line 13 dictionary will be used
    '''
    Gpa calculator based on the credits of the course and the score out of 100
    this function takes in a dictionary like in line 13 and return the semester gpa
    '''
    total_credits = 0 
    keys_as_list = list(g.keys()) 
    for tuple in keys_as_list:
        total_credits+= tuple[1]

    earned = 0 
    for i,j in g.items():
        earned+= grade2gpa(j)* i[1] # e.g ('infs',3): grade2gpa(score) will become 3*score and added to earned
    gpa = earned/total_credits
    return gpa


def ex7():
    '''asks how many times to roll the dice, rolls dice using random module, and 
    saves frequency of each result in a dictionary. 
    note: already imported random in line 108
    '''
    num = input("How many times do you want to roll the dice: ")
    while not (num.isnumeric() and int(num)>0):
        print("positive number please, let's try again")
        num = input("How many times do you want to roll the dice: ")
    num = int(num)

    rolls = []
    
    for i in range(num):
        result = random.randint(1,6)
        rolls.append(result)
    freq = {1:rolls.count(1),2:rolls.count(2),3:rolls.count(3),4:rolls.count(4),5:rolls.count(5),6:rolls.count(6)}
    print(f"Output of dice rolls: {rolls}")
    print(f"Frequency of dice rolls: {freq}")

def ex8():
    '''Takes in amount of money amount and returns a dictionary with keys as
    notes (qatari like 1,5,10,50,100,200,500 QAR) and values as number of notes
    e.g. to get 232 in the smallest number of notes possible we do {200:1,10:3,1:2}
    '''
    amount = input("Enter an amount: ")
    while not(amount.isnumeric() and int(amount)>0):
        print("invalid, please positive amount. try again")
        amount = input("Enger an amount: ")
    amount = int(amount)


    notes = {500:0,200:0,100:0,50:0,10:0,5:0,1:0}
    
    for i in notes.keys():
        print(i,amount)
        while amount>=i and amount>0:
            notes[i] +=1
            amount-=i
            print(amount,i)
    for j in list(notes):
        if notes[j] == 0:
            notes.pop(j)

    return notes
def ex9(attempts):
    '''
takes in attempts, which is list containing student's attempted True/False Questions. and returns a string of the correct answers.
The correct answers made in a such way, so that the average score increases.
Note: The code works as required, but i think the loops are redundant, there's probably a better way to do this, for now at least it works.
'''
    temp = ''
    l = []
    correct = ''
    t = 0
    f = 0
    arranged_scores = []
   # for i in range(len(attempts)): #didn't need this loop
        #attempts[i] = list(attempts[i])
    for i in range(len(attempts[0])):
        for j in range(len(attempts)):
            temp+=attempts[j][i]
        for i in temp:
            
            if i == 'F':
                f+=1
            else:
                t+=1
        
        if f>t:
            correct+='F'
            
        elif f<t:
            correct+='T'
            
        t = 0
        f = 0
        temp = ''
        
    for attempt in attempts: # gonna reuse ex4(attempt, correct) function here
        arranged_scores.append(ex4(attempt,correct))
    print(f"Arranged 'correct' ansers: {correct}")
    print(f"Arranged scores: {arranged_scores}")
    print(f"Best average: {sum(arranged_scores)/len(arranged_scores)}")
    return correct

    
    




# to test ex9() :
attempts=['TTFTTFFTFT','FFFTTFFTFT','TTFFFFFTFT','TTFFFFFTFT','TTFTTTTTFT'
,'TTTTTTTTTT']

print(ex9(attempts))




















    
    

