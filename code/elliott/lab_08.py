a = input('enter your data: ')
data = [int(x) for x in a]


peaks_list = []


for i, element in enumerate(data):
    previous_element = data[i-1] if i > 0 else 0
    current_element = element
    next_element = data[i+1] if i < len(data)-1 else 10
    if previous_element < current_element > next_element:
        peaks_list.append(i)

print(peaks_list)
valley_list = []

for i, element in enumerate(data):
    previous_element = data[i-1] if i > 0 else 0
    current_element = element
    next_element = data[i+1] if i < len(data)-1 else 0
    if previous_element > current_element < next_element:
        valley_list.append(i)

print(valley_list)

print(peaks_list + valley_list)

'''
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]

123456765456789876789 #data

'''
