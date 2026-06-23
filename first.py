import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)


def cleanup_spaces(raw):
    result_list = []
    for i in range(len(raw)):
        if raw[i] == " ":
            continue
        else:
            result_list.append(raw[i])
    return result_list


def list_to_int(list_r):
    return int("".join(map(str, list_r)))


correct = False

while not correct:
    errors = True

    while errors:
        try:
            guess = input("ENTER YOUR GUESS: ")

            # remove spaces -> list of characters
            guess = cleanup_spaces(guess)

            # convert list of characters -> int
            guess = list_to_int(guess)

            errors = False

        except ValueError:
            print("Please enter a whole number")

    if guess == answer:
        correct = True
        print("Well Done, you got it!")
    else:
        diff = abs(guess - answer)

        if 1 <= diff <= 5:
            print("Hot!")
        elif 6 <= diff <= 10:
            print("Warm")
        elif 11 <= diff <= 20:
            print("Cold")
        else:
            print("Freezing")

        if guess > answer:
            print("Lower")
        else:
            print("Higher")