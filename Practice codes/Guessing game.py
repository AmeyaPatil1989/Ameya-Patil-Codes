
while True:
    value = input("Think of a number betwen 1 and 50: ")
    if value.isnumeric() and int(value) < 50 and int (value) > 0:
        while True:
            for counter in range (0,5):
                guess = input("Guess the number or exit if you give up")
                if guess.lower()=="exit":
                    print("You were not able to guess")
                    break
                elif int(guess) > 50 or int(guess) < 0:
                    print("Enter a value between 1 and 50")
                    counter+=1
                    pass
                elif int(value) > int(guess):
                    print("Think of a number higher than this but less than 50")
                    counter+=1
                    pass
                elif int(value) < int(guess):
                    print("Think of a number lower than this but greater than 0")
                    counter+=1
                    pass
                elif int(value) == int(guess):
                    print("You have got it")
                    break
                else:
                    print("Enter a valid value")
                    counter+=1
                    pass
            counter+=1
            break
        print("Number of guesses exceeded the limit")
        break
    else:
        print("Enter a number between 1 and 50")
        pass

print("Thanks for playing")    