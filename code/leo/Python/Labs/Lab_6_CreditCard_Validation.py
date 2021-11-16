

creditcard = (input("please enter your 16 Credit Card Number: ")) #user enter creditcard number
creditcard = creditcard.replace(' ', '') #clean up empty spaces
creditcard = [int(x) for x in creditcard] #turn input into a list of int numbers
last_number_of_creditcard = creditcard.pop(-1) #record last number and remove from list
reversed_creditcard = reversed(creditcard) #reserver list order
reversed_creditcard = list(reversed_creditcard) #turn reserved into list
double_everyother = [y * 2 if index % 2 == 0 else y for index, y in enumerate(reversed_creditcard)] #double every other number in reserved list
minus_nine = [z - 9 if z > 9 else z for z in double_everyother] # Subtract nine from every number larger than 9
sum_of_all = sum(minus_nine) #Sum all values on the list
last_number_of_sum = int(str(sum_of_all)[-1]) #record last number on the sum

if last_number_of_sum == last_number_of_creditcard: #compare last number of the sum with last number of creditcard
    result = "Valid!"
else:
    result = "Not Valid!"

print(creditcard)
print(reversed_creditcard)
print(double_everyother)
print(minus_nine)
print(sum_of_all)
print(result)
