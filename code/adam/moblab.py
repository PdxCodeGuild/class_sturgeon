#MobLab
#Adam, ...
# import time

# print("")
# welcome_message = "Welcome to the Jackalope Simulator?"
# for char in welcome_message:
#   print(char, end='', flush=True)
#   time.sleep(.01)
# time.sleep(.5)
# print("")

#git checkout -b nameofbranch    this creates a new branch
'''
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000
Jackalopes reproduce from 4-8 and die at 10
Gestation is instant, producing 2x offspring
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
represent our population as a list of ints
Jackalopes can only breen once a year
'''
#Dictionary key = population, value = age
# jackalopes = {'population': 2, "age": 0}

jackalopes = [0,0]
year = 2020

while True:
    year += 1
    
    for i, jacks in enumerate(jackalopes):
        jackalopes[i] += 1
        if jacks >= 4 and jacks <= 8:
            jackalopes.append(0)
    while 10 in jackalopes:
        jackalopes.remove(10)
    if len(jackalopes) == 100:
        break
print(jackalopes)
print(year)
    

# age0 = 2
# age1 = 0
# age2 = 0
# age3 = 0
# age4 = 0
# age5 = 0
# age6 = 0
# age7 = 0
# age8 = 0
# age9 = 0
# age10 = 0
# death = 0

# population = 0
# year = 0

# while population <= 1000:
#     year += 1
#     age0 = age1
#     age1 = age2
#     age2 = age3
#     age3 = age4
#     age4 = age5
#     age5 = age6
#     age6 = age7
#     age7 = age8
#     age8 = age9
#     age9 = age10
#     age10 = death

# if x >=4 and x <= 8:
# if x = 10: die