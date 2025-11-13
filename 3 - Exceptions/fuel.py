def main():
    percentage = conversion()
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def conversion():
    while True:
        try:
            fraction = (input("Fraction: "))
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            if x > y:
                # print("continuing")
                continue #pass goes on to the next iteration of a loop
            if x < 0 or y < 0:
                raise ValueError

        except ValueError:
            continue

        try:
            z = x/y
            # print("divided the fraction")
        except ZeroDivisionError:
            # print("passing...")
            continue

            # print("returning a percentage")
        return round((x/y)*100)

main()
