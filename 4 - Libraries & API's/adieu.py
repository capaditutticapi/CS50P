def main():
    names = [] #create an empty list of names
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break #if ctr+D --> exit loop
        names.append(name)
    print("exited")
    convert(names)

def convert(listofnames):
    sentance = "Adieu, adieu, to "
    n = len(listofnames) - 1
    if n == 0:
        sentance = sentance + listofnames[n]
    elif n == 1:
        sentance = sentance + listofnames[0] + " and " + listofnames[1]
    else:
        for i in range(len(listofnames)):
            if i < (n):
                sentance += f"{listofnames[i]}, "
            elif i == (n):
                sentance += f"and {listofnames[i]}"

    print(sentance)

main()
