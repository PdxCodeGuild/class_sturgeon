

nums = []
user_choise_of_numbers = 0

while user_choise_of_numbers != 'done':
    user_choise_of_numbers = input("enter a number, or 'done' ")
    
    if user_choise_of_numbers == 'done':
        break
    else:
        nums.append(int(user_choise_of_numbers))

the_sum_of_user_numbers = 0

for single_numbers_from_nums_list in nums:
    the_sum_of_user_numbers += single_numbers_from_nums_list
    
average = the_sum_of_user_numbers / len(nums)

print(f'The Average is {average}')
