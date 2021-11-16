import string
#create alphabet list with corresponding index
alphabet = [letter for letter in string.ascii_lowercase]

#Asks client to input their word
client_word = input("Would you like to encrypt or unencrypt a word? Please enter the word: ")

#checks index and create a new list
cw_index = [alphabet.index(each) for each in client_word]

#does a little math to assign a new index and then create an output list
transmuted = []
for num in cw_index:
    if num < 13:
        num += 13
        transmuted.append(num)
    elif num >= 13: 
        num -= 13
        transmuted.append(num)
#joins the output list
result = [alphabet[a] for a in transmuted]
#prints answer
answer = "".join(result)
print(f"The process in complete, your word is:  \n{answer}")