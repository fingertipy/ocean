import json

filename = "username.json"
try:
    with open(filename, 'r') as r_obj:
        username = json.load(r_obj)
except FileNotFoundError:
    usernaem = input('What is your name : ')
    with open(filename, 'w') as w_obj:
        json.dump(username, w_obj)
        print("We`ll remeber you when you come back, " + username + "!")
else:
    print('Welcome back, ' + username + '!')