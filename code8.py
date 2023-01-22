word = "banana"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess, keep going until i say it is correct ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You absolute failure")
else:
    print("BRO HOW!")

bruh = input("Press enter to attempt it once again")