"""Lab 6"""
cc_number = "4556737586899855"

def real_card_cherker(cc_number):
    delani = [int(digits) for digits in cc_number]
    print(delani)
    fiji = delani[-1]
    print(fiji) #Test
    delani = delani[:-1]
    print(delani) #Test
    delani.reverse()
    print(delani) #Test
    kenya = []
    for index, value in delani:
        if index%2 == 0: 
            value *= 2
            kenya.append(value)
        else:
            kenya.append(value)        
    print(kenya) #Test
    yosemite = []    
    for x in kenya:
        if x > 9:
           yosemite.append(x-9)
        elif x < 9:
            yosemite.append(x)
    print(yosemite) #Test
    everest = 0
    for each in yosemite:
       everest += each
    print(everest) #test
    whitney = everest%10
    print(whitney) #test
    print(whitney == fiji)

real_card_cherker(cc_number) 
print(real_card_cherker)