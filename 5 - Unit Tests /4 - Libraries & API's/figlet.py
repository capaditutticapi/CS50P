def convert(text, fontname):
    figlet.setFont(font = fontname)
    print(f"Output: \n {figlet.renderText(text)}")
    return

def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        f = random.choice(fonts)     
        convert(text, f)

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            fontname = sys.argv[2]
            if fontname in fonts:
                text = input("Input: ")
                convert(text, fontname)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")


    else:
        print("Invalid usage")
        sys.exit("Invalid usage")

main()
