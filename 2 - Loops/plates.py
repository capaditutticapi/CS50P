def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if starts(s) and maxminchar(s) and endnumb(s) and firstnumb(s) and specialchar(s):
        return True

#starts(): plates must start with at least two letters.”
def starts(s):
    if len(s) < 2:
        return False
    if s[0].isalpha() == True and s[1].isalpha() == True:
        return True
    else:
        return False

#maxminchar(): plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def maxminchar(s):
    if 2 <= len(s) <= 6:
        return True

#endnumb(): Numbers cannot be used in the middle of a plate they must come at the end. ex: AAA222 OK AAA22A not OK
def endnumb(s):
    digitseen = False   
    for characters in s:  
        if characters.isdigit() == True:  
            digitseen = True             
        if characters.isalpha() == True: 
            if digitseen == True:        
                return False
    return True       

#firstnumb(): The first number used cannot be a ‘0’.”
def firstnumb(s):
    for characters in s:
        if characters.isdigit() == True:
            if characters == "0":
                return False
            else:
                return True 
    return True    


#specialchar(): No periods, spaces, or punctuation marks
def specialchar(s):
    for characters in s:
        if characters in[" ", ".", "!","?",]:       
            return False
    return True


main()
