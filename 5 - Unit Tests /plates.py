def main():
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")

def is_valid(s):
    verify = True

    if not (2 <= len(s) <= 6):
        verify = False

    if s[:2].isalpha() == False:
        verify = False

    digitseen = False
    for characters in s:
        if characters.isdigit():
            digitseen = True
        if characters.isalpha():
            if digitseen == True:
                verify = False
                break

    for characters in s:
        if characters.isdigit():
            if characters == "0":
                verify = False
            else:
                break

    for characters in s:
        if characters in[" ", ".", "!","?",]:
            verify = False

    return verify

if __name__ == "__main__":
    main()
