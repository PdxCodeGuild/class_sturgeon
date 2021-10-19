jackalopes = [0,0]
year = 0

while len(jackalopes) <= 1000:
    year += 1
    for i, jack in enumerate(jackalopes):
        jackalopes[i] += 1
        if jack >=4 and jack <= 8:
            jackalopes.append(0)
    while 10 in jackalopes:
        jackalopes.remove(10)

print(year)
print(len(jackalopes))
  