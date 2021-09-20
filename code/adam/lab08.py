# Define the following functions:
# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print("The original list is : " + str(data))

peak_list = []
valley_list = []

def peaks(data):
    peak = 0
    for i in range(1, len(data) - 1):
        if data[i + 1] < data[i] > data[i -1]:
            print(f"{i} is a peak")
            peak_list.append(i)
            peak += 1
    return print(f"Peak Count: {peak} in position(s): {peak_list}")

peaks(data)

print("")

def valleys(data):
    valley = 0
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1]:
            print(f"{i} is a valley")
            valley_list.append(i)
            valley += 1
    return print(f"Valley Count: {valley} in position(s): {valley_list}")

valleys(data)

peaks_and_valleys = peak_list + valley_list
print(f"Peaks and Valleys: {sorted(peaks_and_valleys)}")

j = 0
while int(j) < len(data):
    j += 1
    if j == 8:
        print(19 * " X ")
    if j == 9:
        print(20 * " X ")
else: print("all done")
    # print(f'{i+1}.\t |{data[i]}|')

# #make the list - numbers?
# strings = [str(integer) for integer in data]
# num = "".join(strings)
# integers = int(num)
# print(integers)


# def exes(n):
#     n = ' X ' * int(n)
#     return n
# print(exes(20))