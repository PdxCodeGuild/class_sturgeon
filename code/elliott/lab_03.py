def number_converter(user_choice):
    single = ["", "One", "Two", "Three", "Four",
              "Five", "Six", "Seven", "Eight", "Nine"]

    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["Twenty", "Thirty", "Fourty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]

    if user_choice <= 9:
        return single[user_choice]
    elif user_choice >= 10 and user_choice <= 19:
        return teens[user_choice - 10]
    elif user_choice >= 20 and user_choice <= 99:
        return tens[user_choice//10-2] + '' + single[user_choice % 10]
    elif user_choice >= 100 and user_choice <= 999:
        # use_choice is 500 then this would be 5 hundered
        hund = single[user_choice//100] + ' ' + "hundered"
        # 40 would be 4 (index 4)
        temp = user_choice % 100
        if temp >= 1 and temp <= 9:
            return f'{hund} and {single[temp]}'
        elif temp >= 10 and temp <= 19:
            return f' {hund} and {teens[temp//10-2]}'
        elif temp >= 20 and temp <= 100:
            return f'{hund} and {tens[temp//10-2]} {single[temp % 10]}'
        else:
            return hund


user_choice = int(
    input('Please enter a number that you want to convert to english "1-999". '))
print(number_converter(user_choice))
