groclist = {} #empty DICT
while True:

    try:
        item = input("").upper()
    except EOFError:
        itemsinorder = sorted(groclist.keys())
        for item in itemsinorder:
            print(f"{groclist[item]} {item}")
        break

    if item in groclist.keys():
        groclist[item] = groclist[item] + 1
    else:
        groclist[item] = 1

    continue
