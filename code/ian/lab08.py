data = [1, 2, 3, 4, 5, 4, 6, 1, 2, 3, 4, 5, 4]
# peaks should be [5, 6, 5]
for x in data:
    if data[x-1] < data[x] > data[x+1]:
        print(f'{data[x-1]} < {data[x]} > {data[x-1]}')

   
