#establish starting values
numbers = []
total = 0
number_in = ''

#while list to keep adding numbers to list until done
while True:
    number_in = input("Enter a number or type 'done': ")
    if number_in == 'done':
        break
    numbers.append(float(number_in))

#add each number in the list
for num in numbers:
    total += num

#divide total by the length of the lsit for average
average = total / len(numbers)

#display results
print(f'Average = {average}')
