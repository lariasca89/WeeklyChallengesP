# CX Programming Club
# lariasca
# Weekly Challenge 7
# Module

def password_characters(password):
    """
    Function validates that password doesn't contain . or - at the end and beginning of string
    """
    string = list(password)
    if string[0] == "." or string[0] == "-":
        return False
    elif string[len(string)-1] == "." or string[len(string)-1] == "-":
        return False
    else:
        return True

def password_equals(password1, password2):
    """
    Function validates if both passwords are the same or not. 
    """
    if password1 == password2:
        return True
    else:
        return False

