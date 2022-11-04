import sys

import control
import modes
import sentences
import helpers

def intro():
    sentences.print_word_bank()
    print()
    sentences.example_sentences()
    print()


def select_mode():
    print("Please select mode:")
    print(" 1) Sentence Mode")
    print(" 2) Article Mode")
    print(" 3) Adjective Mode")
    print(" 4) Noun Mode")
    print()

    x = 0
    while not (1 <= x <= 4):
        x = int(input("Selection: "))

    print()
    if x == 1:
        mode = modes.SentenceMode()
    elif x == 2:
        mode = modes.ArticleMode()
    elif x == 3:
        mode = modes.AdjectiveMode()
    elif x == 4:
        mode = modes.NounMode()

    return mode


def select_rounds():
    print("How many rounds would you like to play?")
    rounds = int(input("Selection: "))
    print()
    return rounds


def play_round(mode):
    sample = mode.generate_sample()

    print("Playing sample...")
    helpers.play_sample(sample, sleep=True)
    print()

    print("Type word below. To hear again, press r. If you don't know, type ?")
    print("Your guess: ", end="")
    control.save_pos()

    guess = input()

    while guess == 'r':
        control.restore_pos()
        control.clear_cursor()
        sys.stdout.flush()

        helpers.play_sample(sample, sleep=True)
        guess = input()

    print()
    print("Your guess    : ", guess)
    print("Actual answer : ", sample)

    score = mode.score_sample(guess, sample)
    print()

    print("Enter to play next round, r to hear again: ", end="")
    control.save_pos()

    stuff = input()

    while stuff == "r":
        control.restore_pos()
        control.clear_cursor()
        sys.stdout.flush()

        helpers.play_sample(sample, sleep=True)
        stuff = input()

    return score


def main():
    intro()
    mode = select_mode()
    rounds = select_rounds()

    print(f"Playing {rounds} rounds of {mode}")
    print()

    # Give us extra space so all rounds align
    for x in range(14):
        print()
    for x in range(14):
        control.cursor_up()

    score = 0
    for round_num in range(1, rounds+1):
        print(f"Round {round_num}/{rounds}:")
        print(f"---------")
        score_pct = 0 if round_num == 1 else 100 * score / (round_num - 1)
        print(f"Score: {score_pct:0.0f}%")
        print()
        score += play_round(mode)

        for x in range(14):
            control.cursor_up()
            control.clear_line()

    score_pct = 100 * score / round_num
    print(f"Final Score: {score_pct:0.0f}%")
    print()
    input("Hit enter to exit")

if __name__ == '__main__':
    main()
