

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(data):
    peak = []
    for x in range(len(data)-1):
        if data[x] > data[x - 1] and data[x] > data[x + 1]:
            peak.append(x)
        return peak

def valley(data):
    valley = []
    for x in range(len(data)-1):
        if data[x] < data[x-1] and data[x] < data[x + 1]:
            valley.append(x)
        return valley

x = peak(data) 
y = valley(data)

print(x)
print(y)





#    if data[i] > data[i-1] and data[i] > data[i+1]:
#        peak.append(i)
 

    
#print(f'{data[1]}')
#peak = []

#for x in data:
#    if data[x] > data[x - 1] and data[x] > data[x + 1]:
#        peak.append(x)

#print(peak)