import sys
import csv

if len(sys.argv) == 3:
    try:
        with open(f"{sys.argv[1]}") as inputfile, open(f"{sys.argv[2]}", "w") as outputfile:
            reader = csv.DictReader(inputfile)
            writer = csv.DictWriter(outputfile, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last,first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first":first, "last":last, "house":house})
    except(FileNotFoundError):
        sys.exit("File not found")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
