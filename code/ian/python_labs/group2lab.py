
years = 0
# jacks is age of each jackalope
jacks = [0, 0]


while len(jacks) < 1000:
    for i in range(len(jacks)):
        jacks[i] += 1
        if jacks[i] >= 4 and jacks[i] <= 8:
            jacks.append(0)
        if jacks[i] > 9:
            jacks.remove(jacks[i])
    years += 1
    
        
    
print(f'Pop = {len(jacks)}')
print(f'Years = {years}')













# 0 increase first 4 loops(years)
# for i in list
#i+=1
# if i >= 4 <= 8:
# list.append(0)
#---------------------------
#population = [2]
