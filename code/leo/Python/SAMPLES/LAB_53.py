profile = {
    'username': 'leo',
    'password': 'leo123'
    }


def login(username_attempt, password_attempt):

    if username_attempt == profile['username'] and password_attempt == profile["password"]:
        return True
    else:
        return False


asking = True
x = 0

while asking == True :

    if x >= 3:
       print('\nYour login has been unsuccessful three times! Try again later. Goodbye!\n')
       exit()

    else :
        while x < 3:
            username_attempt = input("\nEnter the username: ")
            password_attempt = input("\nEnter the password: ")
            outcome = login(username_attempt, password_attempt)

            if outcome == True :
                print(f'''
                
                # sucessful login 
                username : {username_attempt} 
                password : {password_attempt} 
            
                Welcome! {username_attempt}!
                ''')
                asking == False
                exit()
                
    
            elif outcome == False and x == 0 :
                x += 1
                print(f'''

                # unsucessful login
            
                username : {username_attempt}
                password : {password_attempt}
        
                Error! Your username or password was incorrect!

                You have 2 login ateempt(s) remainig...
                ''')
            
                while asking == True:
                    question = input('\nWould you like to try again? (yes/no) \n >>')
            
                    if question == 'yes' :
                        asking = True
                        print('\nOk press lets try again!!!')
                        break
            
                    elif question == 'no':
                        asking = False
                        x = 3
                        print('\nOk Good Bye!\n')

                        break
                    elif question != 'yes' or 'no' :
                        print(f'\nYou enter "{question}", that is not a valid enter. Please answer "yes" or "no"...\n')
                        asking = True
                

            elif outcome == False and x == 1 :
                x += 1
                print(f'''

                # unsucessful login
            
                username : {username_attempt}
                password : {password_attempt}
        
                Error! Your username or password was incorrect!

                You have 1 login attempt(s) remainig...
                ''')
            
                while asking == True:
                    question = input('\nWould you like to try again? (yes/no) \n >>')
            
                    if question == 'yes' :
                        asking = True
                        print('\nOk press lets try again!!!')
                        break
            
                    elif question == 'no':
                        asking = False
                        print('\nOk Good Bye!\n')
                        x = 3
                        break
                    elif question != 'yes' or 'no' :
                        print(f'\nYou enter "{question}", that is not a valid enter. Please answer "yes" or "no"...\n')
                        asking = True   


            elif outcome == False and x == 2 :
                x += 1
                print(f'''
                
                # unsucessful login
            
                username : {username_attempt}
                password : {password_attempt}
        
                Error! Your username or password was incorrect!
                ''')          

            elif outcome == False and x == 3:
                break                          