import sys

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    try:
        with open(f"{sys.argv[1]}") as file:
            line_count = 0
            for line in file:
                line = line.strip()
                if line.startswith("#"):       #alternatively, if line[1] == "#":
                    continue
                if line == "":
                    continue
                else:
                    line_count += 1
        print(line_count)
    except(FileNotFoundError):
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
