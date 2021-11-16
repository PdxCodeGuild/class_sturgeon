import random

sheep_to_sleep = random.randint(1,10)

awake = True

sheep = 0

while awake: 
    print(f'{sheep + 1} sheep - baa!')

    sheep += 1

if sheep == sheep_to_sleep:
    awake = False

    # sweet dreams
    print('\n...zZzZzZzZ...')