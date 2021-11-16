data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(nums):
    peaks_list = []
    for i, value in enumerate(nums):
    
        if i == 0 or i == (len(nums))-1:
            pass
        elif nums[i-1] < nums[i] > nums[i+1]:
            peaks_list.append(i)
    return peaks_list
            
def valleys(nums):
    valleys_list = []
    for i, value in enumerate(nums):
    
        if i == 0 or i == (len(nums))-1:
            pass
        elif nums[i-1] > nums[i] < nums[i+1]:
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(nums):    
    p = peaks(nums)
    v = valleys(nums)
    both = p + v
    both.sort()
    print(both)

peaks_and_valleys(data)
