
# Part 1

def linear_search(nums, value):
    
    try:
        return nums.index(value)
    except(ValueError):
        return f'{value} was not fond'


# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 9)
print(index) # 2
