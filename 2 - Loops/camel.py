def main():
    variablename = input("Camel Case: ")
    convert(variablename)

def convert(camel):
    for letters in camel:
        if letters.islower() == True:
            print(letters, end = "")
        elif letters.isupper() == True:
            print("_", letters.lower(), sep = "", end="")
    print() 

main()
