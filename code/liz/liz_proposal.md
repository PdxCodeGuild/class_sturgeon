
Liz's Capstone Proposal


* Name:
    Animal Crossing Critter Collector


* Project Overview:
    Animal Crossing Critter Collector (ACCC) will be a welcomed compainion to any Animal Crossing player. The goal of ACCC is to easily display all the fish, bugs, and sea creatures found in the game and to allow the user to manipulate those critters into caught/uncaught groups. ACCC will also be able tohelp the user know what critter is available to catch at that moment or what the next available. The user will also be able to recieve hints (if they want) to know more logistical information to help them catch their next critter. This application will be made using the Django REST framework, Vue, and an Animal Crossing API.


* Features:
    1. As a game player new to Animal Crossing, I want to see all the fish, bugs, and sea creatures that are available to catch in the game because the game keeps uncaught critters hidden.
        Tasks:
            - Display all the fish, bugs, and sea creatures in an easy to see chart.
            - One chart for each variety of critter
            - Buttons on top to display fish vs bugs vs sea creatures
    
    2. As a dedicated game player, I want to catalog the critters I've caught and see which ones I still need to catch because it will help me play the game.
        Tasks:
            - Store player's caught/uncaught critter lists in database
            - Allow the player to easily click critter icons to mark it as caught/uncaught
            - Display filtered caught/uncaught critters chart(s)(same chart or separate?)
    
    3. As a curious game player, I want to know what critter is available to catch at the current moment or when the next critter is available because I want to play the game more efficiently.
        Tasks:
            - Create a button that, when clicked, allows the player to view a filtered list of currently available critters
            - Create a button that, when clicked, allows the player to view a filtered list of next available critters
    
    4. As a curious game player, I want to know information about a critter I'm trying to catch because it will help me know how to catch it.
        Tasks:
            - Make a hint button that, when clicked, tells the player relevant information to help them better catch a critter (like location, times available, rarity, speed)
    
    5. As a social game player, I want to be able to connect with other ACCC users and compare caught/uncaught critter lists because its more fun with friends!
        Tasks:
            - Allow users to connect with other users
            - Create a user details page to display caught/uncaught critter lists/charts


* Data Model:
    1. User - name, friends(many to many)

    2. Fish - id, name, location, rarity, time, months, shadow size, icon

    3. Bug - id, name, location, rarity, time, months, icon

    4. Sea Creature - id, name, time, months, shadow size, speed, icon


* Schedule:
    Week 1:
        Milestone 1 - App that allows users to signup/signin and view all the available critters
    
    Week 2:
        Milestone 2 - App that allows users to save caught/uncaught data and have button to show what critter is available now
    
    Week 3:
        Milestone 3 - App that has button to show what critter is available next and have a hint button
    
    Week 4:
        Milestone 4 - App that allows users to connect with other users and view eachother's caught/uncaught progress


