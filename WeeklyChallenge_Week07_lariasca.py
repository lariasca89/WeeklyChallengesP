# CX Programming Club
# Weekly Challenge 7
# lariasca
# User Generator Tool

import module1_lariasca as module1

username = {'First': '', 'Second': ''}
passwords = {'First': '', 'Second': ''}

for name in username.keys():
    username[name] = input("Please type the "+name+" user name: ")
    passwordvalidation = True

    while passwordvalidation == True:
        passwords[name] = input("Type the new password: ")
        if module1.password_characters(passwords[name]) == True:
            password2 = input("Type the new password again: ")
            if module1.password_characters(password2) == True:
                if module1.password_equals(passwords[name], password2) == True:
                    passwordvalidation = False
                else:
                    print("Passwords are not the same, try again")
            else:
                print("Incorrect password, . o - are not allowed at the beginning nor at the end")
        else:
            print("Incorrect password, . o - are not allowed at the beginning nor at the end")

print(username, passwords)
