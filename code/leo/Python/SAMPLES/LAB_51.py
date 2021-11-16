profile = {
    'username': 'leo',
    'password': 'leo123'
    }


def login(username_attempt, password_attempt):

    if username_attempt == profile['username'] and password_attempt == profile["password"]:
        return True
    else:
        return False


username_attempt = input("Enter the username: ")
password_attempt = input("Enter the password: ")

outcome = login(username_attempt, password_attempt)

if outcome == True :
    print(f'''
        # sucessful login
        
        username : {username_attempt}
        password : {password_attempt}
        
        Welcome! Your username or password was incorrect!
        ''')
elif outcome == False :
    print(f'''
        # unsucessful login
        
        username : {username_attempt}
        password : {password_attempt}
        
        Error! Your username or password was incorrect!
        ''')