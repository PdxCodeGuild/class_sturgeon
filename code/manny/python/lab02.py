"""Version 1"""

nums = [5, 0, 8, 3, 4, 1, 6]
#Count marker starts at zero
count_marker = 0 
#adds each number to list
for number in nums:
    count_marker += number
    print(count_marker)
#Arithmetic
average_number = count_marker / len(nums)
print(average_number)

"""Version 2"""
average_list = []
counter = 0 

#asks user to input digits or press done.
#Done starts the arithmatic and prints out the average, else the digits are added to the empty list above
while True: 
    list_number = input("Please enter a number, or type 'done' to find the average of all the numbers entered: ")
    if list_number == "done":
        for number in average_list:
            counter += number
        average = counter / len(average_list)
        print(round(average, 3))
        break
    else:
        digits =  float(list_number)
        average_list.append(digits) 