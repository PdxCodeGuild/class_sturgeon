import random

import time

print("")
welcome_message = "Welcome to the Jackalope Simulator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.04)
time.sleep(2)
print("")


def newbaby():
    
    name = ['bob', 'tom', 'jerry', 'sally', 'burger', 'bill', 'hank']
    gender = ['male', 'female']
    
    newjackalope = {}
    newjackalope["name"] = random.choice(name)
    newjackalope["age"] = 0
    newjackalope["sex"] = random.choice(gender)
    newjackalope["pregnant"] = 'no'
    
    return newjackalope
'''
class Jackalope:
    def __init__(self, name, age, sex, pregnant):
        self.name = name
        self.age = age
        self.sex = sex
        self.pregnant = pregnant

jackalope1 = Jackalope('bob', 0, 'male', 'no')
jackalope_dic = {}
jackalope_dic = {'name': jackalope1.name}
for i in jackalope1:
    if jackalope1.pregnant == 'no':
'''

jackalopes = [{'name': "burger", 'age': 0, 'sex': 'female', 'pregnant': 'no'}, {'name': "notburger", 'age': 0, 'sex': 'male', 'pregnant': 'no'}, {'name': "otherburger", 'age': 0, 'sex': 'male', 'pregnant': 'no'}, {'name': "cheeseburger", 'age': 0, 'sex': 'female', 'pregnant': 'no'}]
pregnant = ['yes', 'no']

year = 2021
deathcount = 0
anti_jackal = []
while len(jackalopes) < 1000 and len(jackalopes) != 0:
    year += 1
    for i in range(len(jackalopes)):
        jackalopes[i]['age'] += 1
        if jackalopes[i]['pregnant'] == 'no':
            if i < len(jackalopes)-2:
                if jackalopes[i]['age'] >=4 and jackalopes[i]['age'] <= 8:
                    if jackalopes[i+1]['age'] >=4 and jackalopes[i+1]['age'] <=8:
                        if jackalopes[i]['sex'] == 'female' and jackalopes[i+1]['sex'] == 'male':
                            jackalopes[i]['pregnant'] = 'yes'
                    elif jackalopes[i+2]['age'] >=4 and jackalopes[i+2]['age'] <=8:
                        if jackalopes[i]['sex'] == 'female' and jackalopes[i+2]['sex'] == 'male':
                            jackalopes[i]['pregnant'] = 'yes'
            if i > 2 :
                if jackalopes[i-1]['age'] >=4 and jackalopes[i-1]['age'] <=8:
                    if jackalopes[i]['sex'] == 'female' and jackalopes[i-1]['sex'] == 'male':
                        jackalopes[i]['pregnant'] = 'yes'
                elif jackalopes[i-2]['age'] >=4 and jackalopes[i-2]['age'] <=8:
                    if jackalopes[i]['sex'] == 'female' and jackalopes[i-2]['sex'] == 'male':
                        jackalopes[i]['pregnant'] = 'yes'
        else: 
            jackalopes.append(newbaby())
            jackalopes[i]['pregnant'] = 'no'
    random.shuffle(jackalopes)
    before = len(jackalopes)
    jackalopes = [jack for jack in jackalopes if jack['age'] <= 10]
    deathcount += (before - len(jackalopes))
    anti_jackal.append(deathcount)
    alive = len(jackalopes)
    print(f'\nIn the year{year}')
    print("-----------------")
    print(f'{alive} Jackalopes remain alive')
    print(f'{deathcount} found dead\n')

total_dead = sum(anti_jackal)
print(f'The total deaths of jackalopes is {total_dead}')
if len(jackalopes) >= 1000:
    print(f"In the year {year}, we have a population of {alive} jackalopes")
else:
    print(f"Your population of jackalopes died in the year {year}")