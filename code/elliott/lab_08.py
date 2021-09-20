
a = input('enter your data: ')
data = [int(x) for x in a]


# def Peaks(data):
peaks_list = []

for i in data[1:-1]:  # the pre and post comparison means I have to start from item 2 to second last item
    pre = data.index()
    post = data.index(2)
    if i > data[pre] and i > data[post]:
        peaks_list.append(data.index(i))
   # return peaks_list


print(peaks_list)


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

'''
mylist = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
min = []
for i in mylist[1:-1]:  # the pre and post comparison means I have to start from item 2 to second last item
    pre = data.index(i)-1
    post = data.index(i)+1

    if i < mylist[pre] and i < mylist[post]:

        min.append(mylist.index(i))
    print('min=', min)
'''
