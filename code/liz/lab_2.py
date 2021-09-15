nums = []

while True:
    user_num = input('enter a number, or "done": ')
    if user_num == 'done':
        break
    nums.append(int(user_num))




lst_sum = 0

for num in nums:
    lst_sum += num


print(f"average: {lst_sum/len(nums)}")

    