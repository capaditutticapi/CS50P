import random

def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for j in range(3):
            print(f"{x} + {y} = ", end = "")
            try:
                answer = int(input(""))

                if answer == x + y:
                    score += 1
                    break
            except ValueError:
                pass

            if j < 2:
                print("EEE")
            if j == 2:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

#get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                break
        except ValueError:
            continue
    return lvl

#generate_integer returns a single randomly generated integer > 0 with level digits or raises a ValueError if level is not 1, 2, or 3:
def generate_integer(level):
    if level == 1:
        z = random.randint(0,9)
    elif level == 2:
        z = random.randint(10,99)
    elif level == 3:
        z = random.randint(100,999)
    else:
        raise ValueError("Level is not 1, 2 or 3")
    return z

if __name__ == "__main__":
    main()
