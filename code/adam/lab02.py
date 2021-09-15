#Lab 2: Average Numbers
import time

#Version 1
#Start with the given list, iterate through it, keep a 'running sum', then divide the sum by the elements in list, given by len()

#given list:
# nums = [5, 0, 8, 3, 4, 1, 6] 

# sum_of_nums = 0

# for num in nums:
#     sum_of_nums = sum_of_nums + num
# length = len(nums)
# average = sum_of_nums / length
# nums = str(nums)
# average = str(average)
# print("The average of: " + nums + " is: " + average)


#Version 2
#Ask user to enter numbers into a list one at a time and say 'done', then calculate the average. 

print("")
print("Welcome to the Library-Interface's Average Number Calculator")
time.sleep(1)
print("Enter numbers, one at a time, and the calculator will compute their average")
time.sleep(2)
nums = []
while nums != 'done':
    number = input("Enter a number, or enter 'done'-->")
    if number == 'done':
        # nums.pop() #get rid of the 'done'
        break
    try:
        number = float(number)
        nums.append(number)
    except:
        print('Try again')
    print(nums)

sum_of_nums = 0

for num in nums:
    sum_of_nums += num #**This was annoyingly simple to fix**

length = len(nums)
average = sum_of_nums / length
nums = str(nums)
average = str(average)
print("Calculating...")
calculating = "....... \n....... \n......."
for char in calculating:
    print(char, end='', flush=True)
    time.sleep(.1)
print("")
print("The average of: " + nums + " is: " + average)



