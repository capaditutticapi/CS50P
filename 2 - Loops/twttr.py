def main():
    words = input("Input: ")
    convert(words)
    print("")

def convert(string):
    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            continue
        if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            continue
        else:
            print(letter, end = "")

main()
