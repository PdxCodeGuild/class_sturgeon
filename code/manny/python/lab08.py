test_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(test_data): 
    mountains = []
    for i, num in enumerate(test_data):        
        try:
            if test_data[i -1] < num > test_data[i + 1]:
                mountains.append(i) 
        except IndexError:
            pass
    return mountains

def valley(test_data):
    depressions = []
    for i, num in enumerate(test_data):        
        if i == 0 or i == -1:
            pass    
        else:
            if test_data[i-1] > num < test_data[i+1]:
                depressions.append(i) 
    return(depressions)

def peak_and_valleys(test_data):
    plateu = []

    for i, num in enumerate(test_data):        
        try:
            if test_data[i -1] < num > test_data[i + 1]:
                plateu.append(i) 
        except IndexError:
            pass

    for i, num in enumerate(test_data):        
            if i == 0 or i == -1:
                pass    
            else:
                if test_data[i-1] > num < test_data[i+1]:
                    plateu.append(i)
    plateu.sort()                 
    return(plateu)
