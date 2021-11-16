
def peak(data): #peaks list
    peak = []

    for index in range(len(data) - 1): #add -1 to avoid end of list error
        if data[index] > (data[index - 1]) and data[index] > data[index + 1]: 
            # if item is bigger than item location -1 and item location +1
            peak.append(index)
    return peak

def valley(data): #valley list
    valley = []
    
    for index in range(len(data)):
        if index == 0: # skip first item on the list
            index = index + 1 
        elif data[index] < (data[index - 1]) and data[index] < data[index + 1]:
            #if item is smaller than item location -1 and item location +1
            valley.append(index)
         
    return valley

def peak_and_valley(data):
    peak_and_valley = []

    for index in range(len(data) - 1): #add -1 to avoid end of list error
        if (data[index] > (data[index - 1]) and data[index] > data[index + 1]) or (data[index] < (data[index - 1]) and data[index] < data[index + 1]): 
            # if item is bigger than item location -1 and item location +1
            peak_and_valley.append(index)
    peak_and_valley.pop(0)
    return peak_and_valley



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(f'''
Peak index/es: 
{peak(data)}

Valley index/es: 
{valley(data)}

Peak and Valley index/es: 
{peak_and_valley(data)} 
''')