
def clean_text(x):
    import string
    character = list(string.punctuation)

    for y in character:
        if y in x:
           u = x.replace(y, " ")

    return u.lower().strip().split()


frase = input('Enter the frase you want to clean up: ')

print(clean_text(frase))


