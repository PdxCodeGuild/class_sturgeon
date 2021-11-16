
x = input("Type in your characters for your code: ")
encription_list = list(x)

coder = {
    'a': "n", 'b': "o", 'c': "p", 'd': "q", 'e': "r", 'f': "s", 'g': "t", 'h':  "u",
    'i': "v", 'j': "w", 'k': "x", 'l': "y", 'm': "z", 'n': "a", 'o': "b", 'p': "c",
    'q': "d", 'r': "e", 's':  "f", 't': "g", 'u': "h", 'v': "i", 'w': "j", 'x': "k",
    'y': "l", 'z': "m"

}

encription = []
for i in encription_list:
    encription.append(coder[i])

print(encription)

dec_coder = dict(zip(coder.values(), coder.keys()))

y = input("Type in your code to get the message: ")
decription_list = list(y)

decription = []
for i in decription_list:
    decription.append(dec_coder[i])

print(decription)
