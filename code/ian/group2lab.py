#counter = =0
#digits are age and list total = pop
jacks = [0,0]
pop = len(jacks)
while pop < 1000:
    for i  in jacks:
        if i >= 4 and i <= 8:
            jacks.append(0)
        i += 1
print(pop)
# 0 increase first 4 loops(years)
# for i in list
#i+=1
# if i >= 4 <= 8:
# list.append(0)
#---------------------------
#pop = [2, 0, 0, 0, 2]