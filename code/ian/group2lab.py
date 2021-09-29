counter = 100

jacks = [10, 10, 9, 9, 6, 6, 0, 0]
pop = len(jacks)

for i in range(pop):
    jacks[i] += 1
    if jacks[i] >= 4 and jacks[i] <= 8:
        jacks.append(0)
 #   jacks[i] += 1
    if jacks[i] > 9:
       del jacks[i]
  #  for i in jacks:
   #     i += 1
    
    print(jacks)

print(pop)
print(jacks)














# 0 increase first 4 loops(years)
# for i in list
#i+=1
# if i >= 4 <= 8:
# list.append(0)
#---------------------------
#population = [2]
