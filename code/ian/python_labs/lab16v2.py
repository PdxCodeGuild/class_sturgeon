import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests
import random
import webbrowser

# welcome page
root = tk.Tk()
root.configure(bg="white")
root.geometry("500x500")
root.title("Dinner Decider")

#logo
logo = Image.open('logov3.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="white")
logo_label.image = logo
logo_label.pack()

# Welcome text
instructions = tk.Label(root, text="Welcome to the Dinner Decider!", bg="white", font="Raleway")
instructions.pack()

#chefs choice window
def chef():
    # Open Chef's Window
    win1 = Toplevel()
    win1.title("Chef's Choice")
    win1.configure(bg="white")
    win1.geometry("500x500")
    
    # Input line - location
    e1 =Entry(win1, width=30, bg="#dddddd", font="Raleway")
    e1.pack()
    e1.get()
    
    # Input line label - location
    loc_label = tk.Label(win1, text="Enter Location", bg="white", font="Raleway")
    loc_label.pack()

    # Input line - radius
    e2=Entry(win1, width=30, bg="#dddddd", font="Raleway")
    e2.pack()
    e2.get()
    
    #Input line label - radius
    rad_label = tk.Label(win1, text="Enter Search Radius (miles)", bg="white", font="Raleway")
    rad_label.pack()
    
    # API request w/ user input
    def chef_output():

        results_list= []
        dinner_tags = []

        # Variables to store user input for request
        where = e1.get()
        radius = (int(e2.get()) * 1609)
        
        # Request
        response = requests.get('https://api.yelp.com/v3/businesses/search',
        headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer gZUmTUzsgiDZ1sDhj6UME7_MwIK7TLO1t49_iLv3IFyo-whfnB4UNHyJ2xgBXF7mpqmjJU-je_R4wLoSmcJl7oYZdEghY7LUOtSsdjMHO6LK3YmkHmKC0mbYDpdcYXYx'},
        params={
            "location": where,
            "radius": radius})
        
        data = response.json()

        # Store reults in list
        for i in data['businesses']:
            results_list.append(i)

        # Select random from results
        global dinner
        dinner = random.choice(results_list)

        # Store categories for selected result
        for item in dinner['categories']:
            dinner_tags.append(item['title'])

        # Result output text
        result_text1 = "\n"+dinner['name'] + "\n" + "\n" + "Rating - " + str(dinner['rating']) +"\n" + "Tags - " + str(dinner_tags)
        result_text2 = "Address:" + "\n" + str(dinner['location']['display_address']) + "\n" + "Phone:" + "\n" + str(dinner['display_phone'] + "\n")
    
        # Configure labels after request
        o1_label.configure(text=result_text1)
        o2_label.configure(text=result_text2)
        order_btn.configure(state=tk.NORMAL, bg='#d94423', fg="white")

    def order():
            webbrowser.open(dinner['url'])

    # Let's eat button (calls API request/output)
    le_btn = tk.Button(win1, text="Let's Eat", command=chef_output, bg='#d94423', fg='white', font="Raleway", height=2, width=15)
    le_btn.pack()
    
    #Placeholder labels (Updates  w/ configure)
    o1_label = tk.Label(win1, text='', bg="white", font="Raleway")
    o1_label.pack()
    o2_label = tk.Label(win1, text='', bg="white", font="Raleway" )
    o2_label.pack()

    # Order button (links url, disabled till 1st config)
    order_btn = tk.Button(win1, text="Order", command=order, state=tk.DISABLED, bg="gray", fg="black", font="Raleway", height=2, width=15)
    order_btn.pack()

    # Back button
    back_btn = tk.Button(win1, text="Back", command=win1.destroy, bg='#d94423', fg="white", font="Raleway", height=2, width=15)
    back_btn.pack()
    
# Search window
def search():
    
    # Open search window
    win2 = Toplevel()
    win2.title("Search")
    win2.configure(bg="white")
    win2.geometry("500x500")
    
    # Input line - location
    e3 =Entry(win2, width=30, bg="#dddddd", font="Raleway")
    e3.pack()
    e3.get()
    
    # Input line label - location
    loc_label = tk.Label(win2, text="Enter Location", bg="white", font="Raleway")
    loc_label.pack()

    # Input line - radius
    e4=Entry(win2, width=30, bg="#dddddd", font="Raleway")
    e4.pack()
    e4.get()
    
    # Input line label - radius
    rad_label = tk.Label(win2, text="Enter Search Radius (miles)", bg="white", font="Raleway")
    rad_label.pack()

    # Input line - category
    e5=Entry(win2, width=30, bg="#dddddd", font="Raleway")
    e5.pack()
    e5.get()

    # Input line label - category
    cat_label = tk.Label(win2, text="Search Category", bg="white", font="Raleway")
    cat_label.pack()

    # API request with more input params
    def search_output():

        results_list= []
        dinner_tags = []

        # Variables to store user input
        where = e3.get()
        radius = (int(e4.get()) * 1609)
        s_term = e5.get()
        
        # Request
        response = requests.get('https://api.yelp.com/v3/businesses/search',
        headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer gZUmTUzsgiDZ1sDhj6UME7_MwIK7TLO1t49_iLv3IFyo-whfnB4UNHyJ2xgBXF7mpqmjJU-je_R4wLoSmcJl7oYZdEghY7LUOtSsdjMHO6LK3YmkHmKC0mbYDpdcYXYx'},
        params={
            "location": where,
            "radius": radius,
            "term": s_term})
        
        data = response.json()

        # Store results in list
        for i in data['businesses']:
            results_list.append(i)

        # Select random from list
        global dinner
        dinner = random.choice(results_list)

        # Store categories for result
        for item in dinner['categories']:
            dinner_tags.append(item['title'])

        # Result text
        result_text3 = "\n"+dinner['name'] + "\n" + "\n" + "Rating - " + str(dinner['rating']) +"\n" + "Tags - " + str(dinner_tags)
        result_text4 = "Address:" + "\n" + str(dinner['location']['display_address']) + "\n" + "Phone:" + "\n" + str(dinner['display_phone'] + "\n")
         
        # Configure labels after request
        o3_label.configure(text=result_text3)
        o4_label.configure(text=result_text4)
        order_btn.configure(state=tk.NORMAL, bg='#d94423', fg="white")

    def order():
            webbrowser.open(dinner['url'])

    # Let's eat button (calls request/output)
    le_btn = tk.Button(win2, text="Let's Eat", command=search_output, bg='#d94423', fg='white', font="Raleway", height=2, width=15)
    le_btn.pack()

    # Placeholder labels (Updates w/ config)
    o3_label = tk.Label(win2, text='', bg="white", font="Raleway")
    o3_label.pack()
    o4_label = tk.Label(win2, text='', bg="white", font="Raleway" )
    o4_label.pack()

    # Order button (Links url, disabled till first config)
    order_btn = tk.Button(win2, text="Order", command=order, state=tk.DISABLED, bg="gray", fg="black", font="Raleway", height=2, width=15)
    order_btn.pack()

    # Back button
    back_btn = tk.Button(win2, text="Back", command=win2.destroy, bg='#d94423', fg="white", font="Raleway", height=2, width=15)
    back_btn.pack()

# Chef's choice button (calls Chef's choice window)
btn1_btn = tk.Button(root, text="Chef's Choice", command=lambda:chef(), bg='#d94423', fg='white', font="Raleway", height=2, width=15)
btn1_btn.pack()

# Search button (calls Search window)
btn2_btn = tk.Button(root, text="Search", command=lambda:search(), bg='#d94423', fg='white', font="Raleway", height=2, width=15)
btn2_btn.pack()

# Exit button (closes program)
btn3_btn = tk.Button(root, text="Exit", command=root.quit, bg='#d94423', fg='white', font="Raleway", height=2, width=15)
btn3_btn.pack()

root.mainloop()