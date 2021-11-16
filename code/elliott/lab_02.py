
total = 0
count = 0


while True:
    i = input('Enter a number or "done": ')
    if i == "done":
        break
    else:
        total += float(i)
        count += 1
        average = total / count

print('Your average: ', average)
