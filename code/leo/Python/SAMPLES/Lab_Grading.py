'''
Let's convert a numerical score into a letter grade, using if and elif statements and comparisons.

Have the user enter a number representing the score (0-100)
Convert the score to a letter grade A - F
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F

'''

score = input("Please enter your score (0-100) to find out your grade (A-F): ")
score = int(score)

if score > 100 :
    print("Error, please enter value between 0 and 100")

elif score < 0 :
    print("Error, please enter value between 0 and 100")

elif score >= 90 :
    print("Congradulations! Your grade is A")

elif score >= 80 :
    print("Good Job! Your grade is B")

elif score >= 70 :
    print("You passed! Your grade is C")

elif score >= 60 :
    print("You almost made it! Your grade is D")

elif score < 60 :
    print("Oh no! Unfortunatelly you failed this time, your grade is F")
