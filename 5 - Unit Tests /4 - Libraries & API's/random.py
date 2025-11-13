from random import choice

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue 

seq = range(1, n+1)
x = choice(seq)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < x:
        print("Too small!")

    elif guess > x:
        print("Too large!")

    elif guess == x:
        print("Just right!")
        break
