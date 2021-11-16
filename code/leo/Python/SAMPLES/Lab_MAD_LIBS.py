'''
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

It can be a little tricky to find a plain-text Mad Lib that's easy to copy and paste. Instead, choose some song lyrics, a poem or quote, or create your own story.

Instructions:
Choose some text to act as your Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use an f-string to put each word into the Mad Lib

'''



print("Welcome to Mad Lib")

adj = input("With one word, enter how you felt today after learning about variable: ")
noun1 = input("What animal will you reincarnated in your next life? ")
noun2 = input("Favor place in your house: ")
numb = input("How far you can count without inhaling? Enter the number: ")
verb = input("Enter a verb ending with \"ing\": ")
action = input ("What would be your first reaction if Jeffrey Bezos just walked into your room, right now?: ")
thing = input("What is your favor thing you have? ")

message = f'''
Why is there a {adj} {noun1} in your {noun2}?
If you don't stop {verb} and start cleaning it up 
by the time I count to {numb}, I swear I'm going to {action} your {thing}!
'''

print(message)





