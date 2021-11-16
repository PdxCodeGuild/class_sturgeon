#Lab03 Number to Phrase Converter
#This will allow numbers from zero to 999 to be converted to word form.
import time

print("")
welcome_message = "Welcome to the Library-Interface's Number to Phrase Converter"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
print("")


#two lists for the unique english words 1-19, the decades and centuries to cover everything to a thousand
number_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teen_list = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decades_list =["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
#So glad I'm not doing Fench, 60+17 (77) and 4+20+16 (96) are hard enough to explain to people without coding it
centuries_list =["hundred"]

#because the lists start with zero above, this works under twenty
def number_conversion(number):
    if number <= 9:
        print(number_list[number].capitalize())
    elif number >= 10 and number <= 19:
        tens = number % 10
        print(teen_list[tens].capitalize())
    #At twenty we get a '2', which doesn't work with the zero based python, so we have to minus the 2 off
    elif number > 19 and number <= 99:
        ones = number // 10
        correction_over_20 = ones - 2
        tens = number % 10
        if tens == 0:
            print(decades_list[correction_over_20].capitalize())
        elif tens != 0:
            print(decades_list[correction_over_20].capitalize() + " " + number_list[tens])
    #It's easier to just make this one unique
    elif number == 100:
        print("One Hundred")
    #Making 400 turn into 4 for the 'four hundred' is done by //10 //10 the number
    elif number > 100 and number < 109:
        hundreds = number // 10 // 10
        ones = number % 10
        my_string = f"{number_list[hundreds]} hundred and {number_list[ones]}".capitalize()
        print(my_string)
    elif number >= 110 and number <= 119:
        hundreds = number // 10 // 10
        teenie = number % 10
        my_string1 = f"{number_list[hundreds]} hundred and {teen_list[teenie]}"
        print(my_string1.capitalize())
    elif number >= 120 and number < 1000:
        hundreds = number // 100 #haha, this works
        ones = number % 10
        tens = number % 100 // 10 - 2 #not sure why this works, but trial and error shows that it does
        my_string2 = f"{number_list[hundreds]} hundred and {decades_list[tens]} {number_list[ones]}"
        print(my_string2.capitalize())
        
while True:
    number = input("Enter a whole number 0 through 999-->")
    try:
        number = float(number)
        if number >= 0 and number <= 1000:
            number = int(number)
            number_conversion(number)
            if input("Again?-->") != "yes":
                break
        else:
            print('The number must be between 0 and 999, try again')
            continue
    except:
        print('Try again. Enter a number between 0 and 999')
print("Thank you for using the Number to Phrase Converter.")