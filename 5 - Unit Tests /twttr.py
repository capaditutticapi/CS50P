def main():
    words = input("Input: ")
    print(shorten(words))

def shorten(word):
    output = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            continue
        else:
            output += letter
    return (output)



if __name__ == "__main__":
    main()
