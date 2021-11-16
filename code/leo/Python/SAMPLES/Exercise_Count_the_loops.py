
counter = 0

while True :
    counter += 1
    again = input('Add to the count again? yes/no ')

    if again == 'no':
        print(f'The loop ran {counter} times.')

        break

