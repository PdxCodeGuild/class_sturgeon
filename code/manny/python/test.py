from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
# import requests
import random


words_testing = ['academic', 'academics', 'academy', 'acc', 'accent', 'accept', 'acceptable', 'acceptance', 'accepted', 'accepting', 'accepts', 'access', 'accessed']

"""words = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
words = words.text.split()"""

hangman = random.choice(words_testing)
while len(hangman) < 7:
    hangman = random.choice(words_testing)
else:
    pass

secret_word = [each for each in hangman]
units = len(secret_word)
print(secret_word)

root = Tk()
root.title("Hangman!")
mainframe = ttk.Frame(root, padding=100)

hangman_1 = ImageTk.PhotoImage(Image.open("images/hangman1.png"))
hangman_2 = ImageTk.PhotoImage(Image.open("images/hangman2.png"))
hangman_3 = ImageTk.PhotoImage(Image.open("images/hangman3.png"))
hangman_4 = ImageTk.PhotoImage(Image.open("images/hangman4.png"))
hangman_5 = ImageTk.PhotoImage(Image.open("images/hangman5.png"))
hangman_6 = ImageTk.PhotoImage(Image.open("images/hangman6.png"))
hangman_7 = ImageTk.PhotoImage(Image.open("images/hangman7.png"))
game_win = ImageTk.PhotoImage(Image.open("images/win.png"))

picture_list = [hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7]
order = 0
my_image = Label(image=picture_list[order])
my_image.grid(row=0, column=0, columnspan=3)

welcome_text = f"Today's mystery word has {units} characters. Please input your guesses below."
welcome = Label(root, text = welcome_text)
welcome.grid(row = 1, columnspan=3)

guess = Entry(root, width= 10, borderwidth=3)
guess.grid(row=3, column= 1)

blank = "_"
blank_list = []

for i in range(units):
    blank_list.append(blank)

blank_spots = Label(root, text=blank_list)
blank_spots.grid(row=2, column =1)

def popup():
    messagebox.showinfo("I literally said not to press this.")

def game():
    global order
    global my_image
    global secret_word
    global blank_list
    global blank_spots

    entry = guess.get()
    positive_response = "That letter is in there"
    negative_response = "Not there. Try again."
    
    game_counter = len(secret_word)


    letter_counter = secret_word[:]

    if entry in secret_word:
        response = positive_response
        
        place = []
        count = 0
        
        for each in secret_word:
            if each == entry:
                place.append(count)
                game_counter = game_counter -1 
            count +=1

        for i in place:
            blank_list[i] = entry
        
        print(secret_word)
        print(letter_counter)
        print(game_counter)
    
    else:
        response = negative_response
        order = order + 1

    game_text = f"You have chosen the letter {entry}. {response}. "
    game_label = Label(root, text = game_text)
    game_label.grid(row = 4, columnspan= 4)
    
    my_image.forget()
    my_image = Label(image=picture_list[order])
    my_image.grid(row=0, column=0, columnspan=3)

    blank_spots.forget()
    blank_spots = Label(root, text=blank_list)
    blank_spots.grid(row=2, column =1)
    if blank_list != secret_word:
        return

    else:
        my_image.forget()
        my_image = Label(image=game_win)
        my_image.grid(row=0, column=0, columnspan=3)
    
ttk.Button(root, text="Quit", command = root.destroy).grid(row=5, column=0)
ttk.Button(root, text="Don't press", command=popup).grid(row=5, column=2)
ttk.Button(root, text="Let's play hangman!", command = game).grid(row=5, column=1)

root.mainloop()