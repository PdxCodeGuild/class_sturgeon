# peaks and valleys

def peaks (data):
    peaks = []
    for i, value in enumerate(data):
        if i == 0 or i == len(data) - 1:
            pass
        elif value > data[i - 1] and value > data[i + 1]:
            peaks.append(i)
    return peaks
   
        

def valleys (data):
    valleys = []
    for i, value in enumerate(data):
        if i == 0 or i == len(data) - 1:
            pass
        elif value < data[i - 1] and value < data[i + 1]:
            valleys.append(i)
    return valleys


def peaks_and_valleys (data_peaks, data_valleys):
    data_peaks.extend(data_valleys)
    return sorted(data_peaks)
   


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

data_peaks = peaks(data)
#print(data_peaks)
data_valleys = valleys(data)
#print(data_valleys)
data_peaks_and_valleys = peaks_and_valleys(data_peaks, data_valleys)
print(data_peaks_and_valleys)

# this is not correct. i need to figure out how to create a new line between each loop
for i in range(9, 0, -1):
    for j in data:
        if j >= i:
            print('X', end='')
        else:
            print(' ', end='')
        





