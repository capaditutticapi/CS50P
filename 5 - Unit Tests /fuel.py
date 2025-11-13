import sys

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    if not percentage == None:
        print(gauge(percentage))

def convert(fraction):
    fraction = fraction.split("/")
    try:
        x = int(fraction[0])
        y = int(fraction[1])
    except(ValueError):
        return 
    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
