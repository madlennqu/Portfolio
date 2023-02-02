import random

list = ["apple", "banana", "grape", "blueberry", "raspberry"]
choice = random.choice(list)
end_of_game = False
lives = 6

display = []
for _ in range(len(choice)):
    display += "_"
    
while not end_of_game:
    guess = input("Please type a letter: ").lower()

    if guess in display:
        print("You have already guess it")
    for position in range(len(choice)):
        letter = choice[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    if guess not in choice:
        print(f"Your guess {guess} is not correct. You lose")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True
        print("You win")
        print(f"You found a word. The solution is {choice}")
