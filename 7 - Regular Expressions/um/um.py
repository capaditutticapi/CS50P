import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    if ums := re.findall(r"\bum\b", s, flags = re.IGNORECASE):
        return len(ums)

    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
