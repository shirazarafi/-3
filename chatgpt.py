import random

def generate_code():
    """Generate a random 4-digit code with digits from 0 to 9."""
    return [random.randint(0, 9) for _ in range(4)]

def get_feedback(code, guess):
    """Provide feedback on the user's guess.
    Returns the number of bulls (correct digit and position) and cows (correct digit, wrong position).
    """
    bulls = sum([code[i] == guess[i] for i in range(4)])
    cows = sum([min(code.count(digit), guess.count(digit)) for digit in set(guess)]) - bulls
    return bulls, cows

def play_game():
    """Run the Bull and Cow game."""
    print("\u05d1\u05d5\u05dc \u05e4\u05d2\u05d9\u05e2\u05d4 \u2013 \u05d1\u05e8\u05d5\u05da \u05dc\u05e0\u05d7\u05e9!\n")
    print("\u05e2\u05dc\u05d9\u05da \u05dc\u05e0\u05d7\u05e9 \u05e7\u05d5\u05d3 \u05e1\u05d5\u05d3 \u05e9\u05dc 4 \u05e1\u05e4\u05e8\u05d5\u05ea \u05de-0 \u05e2\u05d3 9. \u05d4\u05e9\u05d0 \u05dc\u05da \u05e9\u05de\u05d5\u05e0\u05d4 8 \u05e0\u05d9\u05e1\u05d9\u05d5\u05e0\u05d5\u05ea.\n")

    code = generate_code()
    attempts = 8

    while attempts > 0:
        try:
            guess = input(f"\u05d4\u05db\u05e0\u05e1 \u05d0\u05ea \u05e0\u05d7\u05e9 \u05d4\u05de\u05e1\u05e4\u05e8 \u05d4\u05d1\u05d0\u05e8\u05d1 (\u05d9\u05e9 \u05dc\u05da {attempts} \u05e0\u05d9\u05e1\u05d9\u05d5\u05e0\u05d5\u05ea): ")
            if len(guess) != 4 or not guess.isdigit():
                print("\u05d1\u05d1\u05e7\u05e9\u05d4: \u05d0\u05ea \u05e6\u05e8\u05d9\u05da \u05dc\u05d4\u05db\u05e0\u05d9\u05e1 \u05e8\u05e7 4 \u05e1\u05e4\u05e8\u05d5\u05ea!\n")
                continue

            guess = [int(digit) for digit in guess]
            bulls, cows = get_feedback(code, guess)

            if bulls == 4:
                print("\u05d1\u05e8\u05db\u05d5 \u05e0\u05e6\u05d7\u05ea \u05d0\u05ea \u05d4\u05e7\u05d5\u05d3! \u05d0\u05ea\u05d4 \u05d0\u05dc\u05d5\u05e3!\n")
                break

            print(f"\u05de\u05e1\u05e4\u05e8 \u05e0\u05db\u05d5\u05e0\u05d5\u05ea: {bulls}, \u05e4\u05e8\u05d5\u05ea \u05e0\u05db\u05d5\u05e0\u05d5\u05ea: {cows}\n")
            attempts -= 1

        except Exception as e:
            print("\u05d7\u05dc\u05e7 \u05e7\u05e8\u05d4! \u05e0\u05e1\u05d4 \u05dc\u05e0\u05e1\u05d5\u05ea \u05e9\u05d5\u05d1!\n")

    if attempts == 0:
        print("\u05dc\u05e6\u05e2 \u05d4\u05e0\u05e1\u05d9\u05d5\u05e0\u05d5\u05ea. \u05d4\u05e7\u05d5\u05d3 \u05d4\u05d0\u05de\u05d9\u05ea \u05d4\u05d9\u05d4: ", ''.join(map(str, code)))

if __name__ == "__main__":
    play_game()
