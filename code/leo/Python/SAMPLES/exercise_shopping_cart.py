fruits = {
    'apple': 0.65,
    'banana': 0.5,
    'guava': 0.33
}


shopping_basket = {
    'apple': 4,
    'banana': 6,
    'guava': 8
}

total = 0

for fruit in shopping_basket : #loop through each fruit
    quantity = shopping_basket[fruit] # get the quanity from shopping basket
    sub_total = quantity * fruits[fruit] # quantity * price

    total += sub_total # add subtotal 

    print(f'{quantity} {fruit} : ${sub_total}')
print("-----------")
print(f'Total: ${total}')
