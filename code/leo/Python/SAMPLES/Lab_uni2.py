

def sum_numbers(numbers) :
    
    sum_of_numbers = 0

    for x in numbers:
        sum_of_numbers += x

    return sum_of_numbers


list_of_numbers = []

user_input = 0
answer = True

while answer == True :
    try:
        user_input = int(input("Enter a number or 'done' to quit: "))

        if user_input != 'done' :
            list_of_numbers.append(user_input)

        else :
            answer = False
            break
    except ValueError:
            break


print(f'Your entered {list_of_numbers}')

print(f'The sum of the numbers is {(sum_numbers(list_of_numbers))}')







