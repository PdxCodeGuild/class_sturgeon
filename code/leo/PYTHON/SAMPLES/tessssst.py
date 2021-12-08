import random

forcode = ['a','b','c','d']

code = list()
for x in range(3):
    code.append(random.choice(forcode))

code = ''.join(code)
code = str('http:www.'+ code + '.com')

print(code)
