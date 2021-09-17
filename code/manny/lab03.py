"""Lab 3"""
#Dictionary uses key value pairs to create number strings 

num_dict = {
    0 : "zero",
    1 : "one",
    2 : "two", 
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}    

tens_dict = {
    20 : "twenty", 
    30 : "thirty",
    40 : "fourty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
}

#Ensures the user input was an int 
while True: 
    try:
        user_input = int(input("Please input a number between 0-999 and I'll tell you how it's written out in English! "))
        print("Thank you! Calculating...")
        break
    except ValueError:
            print("Please follow directions next time.") 
            break

#Checks if input is in either of both dictionaires and if not, breaks them down, searches keys and then puts the strings together. 
if user_input <=99:   
    if user_input in num_dict:
        print(num_dict[user_input])
    elif user_input in tens_dict:
        print(tens_dict[user_input])
    elif user_input//10 != 0 and user_input%10 != 0: 
        tens_digit = (user_input//10) * 10
        ones_digit = user_input%10 
        if tens_digit in tens_dict:
            tens_answer = tens_dict[tens_digit]
        if ones_digit in num_dict: 
            ones_answer = num_dict[ones_digit]
        print(f"{tens_answer}-{ones_answer}")
    else: 
        print("Give me more time!")
elif user_input <= 999: 
    if user_input%100 == 0:
        hundreths_digit = user_input//100
        if hundreths_digit in num_dict:
            hundreths_answer = num_dict[hundreths_digit]
            print(f"{hundreths_answer} hundred")
    elif user_input//100 != 0: 
        hundreths_digit = user_input//100
        if hundreths_digit in num_dict: 
            hundred_answer = num_dict[hundreths_digit]
        while user_input > 100: 
            user_input -= 100
            if user_input in num_dict:
                rebel_teen = num_dict[user_input]
                print(f"{hundred_answer} hundred {rebel_teen}")
            elif user_input > 100: 
                tens_digit = (user_input//10) * 10
                ones_digit = user_input%10 
                if tens_digit in tens_dict:
                    tens_answer = tens_dict[tens_digit]
                if ones_digit in num_dict: 
                    ones_answer = num_dict[ones_digit]
                while True: 
                    try: 
                        print(f"{hundred_answer} hundred {tens_answer}-{ones_answer}")
                        break
                    except NameError: 
                        print(f"{hundred_answer} hundred and {ones_answer}")
                        break
else:
    print("That's too many numbers!")

