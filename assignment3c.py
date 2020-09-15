def num_guess():
    num = int(input("Enter a number for the player to guess: "))
    guess = int(input("Enter your guess: "))
    count = 0
    
    while guess != num:
        if guess > num:
            count += 1
            print("Too high - Try again")
            guess = int(input("Enter your guess: "))
        elif guess < num:
            count += 1
            print("Too low - Try again")
            guess = int(input("Enter your guess: "))
    print(f"Correct! you guessed it in {count} tries")

num_guess()