#1
card_num = list(input('Enter a card number: '))
print(f'Card num - {card_num}')
#2
check_digit = int(card_num.pop())
print(f'Check digit - {check_digit}')
#3
reversed_card = card_num[::-1]
print(f'Reversed Card - {reversed_card}')
#4
double = [int(num)*2 if i%2==0 else int(num) for i, num in enumerate(reversed_card)]
print(f'Doubles - {double}')

#5
nines = [num-9 if num>9 else num for num in double]
print(f'Nines - {nines}')

#6
sum = sum(nines)
print(f'sum- {sum}')

#7
second_digit = sum%10
print(f'second digit - {second_digit}')

#8
if second_digit == check_digit:
    print('Valid')
else:
    print('Not a valid card')

