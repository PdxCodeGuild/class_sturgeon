import random

def newbaby():
    
    name = ['bob', 'tom', 'jerry']
    gender = ['male', 'female']
    
    newjackalope = {}
    newjackalope["name"] = random.choice(name)
    newjackalope["age"] = 0
    newjackalope["sex"] = random.choice(gender)
    newjackalope["pregnant"] = 'no'
    
    return newjackalope


jackalopes = [{'name': "burger", 'age': 0, 'sex': 'female', 'pregnant': 'no'}, {'name': "notburger", 'age': 0, 'sex': 'male', 'pregnant': 'no'}]
pregnant = ['yes', 'no', 'maybe']

#jackalopes = [0,0]
year = 0

while len(jackalopes) <= 1000:
    year += 1
    
    for i, jack in enumerate(jackalopes):
        jack['age'] += 1
        if jack['age'] >=4 and jack['age'] <= 8:
            jackalopes.append(newbaby())
    random.shuffle(jackalopes)
    jackalopes = [jack for jack in jackalopes if jack['age'] <= 10]
    

    #while jackalopes.values['age'] == 10 in jackalopes:
     #   jackalopes.remove(10)

print(f"It will take {year} years to build a population of 1000 jackalopes")
print(jackalopes)
