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

while asking == True :
    
    username_attempt = input("Enter the username: ")
    password_attempt = input("Enter the password: ")
    outcome = login(username_attempt, password_attempt)

    if outcome == True :
            print(f'''
            # sucessful login 
            username : {username_attempt} 
            password : {password_attempt} 
            
            Welcome! {username_attempt}!
            ''')
            asking == False
            break
    
    elif outcome == False :
            print(f'''
            # unsucessful login
            
            username : {username_attempt}
            password : {password_attempt}
        
            Error! Your username or password was incorrect!
            ''')
            
            while asking == True:
                question = input('Would you like to try again? (yes/no) \n >>')
            
                if question == 'yes' :
                    asking = True
                    print('Ok press lets try again!!!')
                    break
            
                elif question == 'no':
                    asking = False
                    print('Ok Good Bye!')
                    break
                elif question != 'yes' or 'no' :
                    print(f'You enter "{question}", that is not a valid enter...')
                    asking = True



                