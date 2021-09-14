import time
from colorama import Fore, Back, Style

message = 'hello world!'
for char in message:
  print(char, end='', flush=True)
  time.sleep(.1)
    

print(Fore.RED + 'this is red text')
print(Back.BLUE + 'this is red text on a blue background')
print(Style.RESET_ALL)
print('back to normal')

print(.1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 == 1.0) #this will come out false
print(.3 + .3 + .3 == .9) #again, this is false
print(.4 + .4 == .8) #this is true, only one math thing involved it doesn't suck
print (.1 + .2 + .3 == .6) #false, wow, even different numbers. it hates more than one maths. 

a = .1
b = .2
c = .3
print(a + b + c == .6) #false, it really hates this.

print(4 == 4 > 2 < 5 != 8 < 11 -2 + 9 == 9 * 2) #true

d = ['cheese', 'apple']
e = d
d.append('pinapple') # notice how pinapple is added to both e and d because e isn't unique
print(d)
print(e)

#Using shorthand
temp = 65
thing_we_should_do = "turn on the heat" if temp < 67 else "keep the heat off"
print(thing_we_should_do)
print("I love the cold" if temp < 80 else "I hate the heat")

#while loop
i = 5
while i > 0:
    print(i, end=' mississippi ')
    i -= 1
print(' Ready or not, here I come!')

