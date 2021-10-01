import random


def newbaby():
    
    name = ['bob', 'tom', 'jerry', 'sally', 'burger', 'bill', 'hank']
    gender = ['male', 'female']
    
    newjackalope = {}
    newjackalope["name"] = random.choice(name)
    newjackalope["age"] = 0
    newjackalope["sex"] = random.choice(gender)
    newjackalope["pregnant"] = 'no'
    
    return newjackalope

jackalopes = [{'name': "burger", 'age': 0, 'sex': 'female', 'pregnant': 'no'}, {'name': "notburger", 'age': 0, 'sex': 'male', 'pregnant': 'no'}, {'name': "otherburger", 'age': 0, 'sex': 'male', 'pregnant': 'no'}, {'name': "cheeseburger", 'age': 0, 'sex': 'female', 'pregnant': 'no'}]
pregnant = ['yes', 'no']

year = 0

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
    jackalopes = [jack for jack in jackalopes if jack['age'] <= 10]
    print(len(jackalopes))
# print(jackalopes)
if len(jackalopes) >= 1000:
    print(f"It will take {year} years to build a population of 1000 jackalopes")
else:
    print(f"Your population died at year {year}")

