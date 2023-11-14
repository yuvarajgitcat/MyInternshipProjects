def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a small village with rumors of a mystical artifact.")
    print("Your objective is to find the artifact and return it to the village.")
    print("Be careful, as your choices will determine your fate!")

def make_choice(options):
    while True:
        print("\nChoose your path:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_path():
    print("\nYou enter a dark forest. The path splits ahead.")
    options = ["Follow the left path", "Follow the right path"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou discover a hidden cave with a sleeping dragon. What do you do?")
        options = ["Attempt to sneak past the dragon", "Wake up the dragon"]
        choice = make_choice(options)

        if choice == 1:
            print("\nYou successfully sneak past the dragon. The left path leads to the artifact!")
            return "success"
        else:
            print("\nThe dragon wakes up and attacks you. Game over!")
            return "game_over"

    else:
        print("\nYou encounter a group of bandits. What do you do?")
        options = ["Fight the bandits", "Try to negotiate"]
        choice = make_choice(options)

        if choice == 1:
            print("\nYou decide to confront the bandits, but they overpower you. Game over!")
            return "game_over"
        else:
            print("\nYour negotiation skills impress the bandits, and they let you pass. The right path leads to the artifact!")
            return "success"

def mountain_path():
    print("\nYou climb a steep mountain. There's a fork in the path ahead.")
    options = ["Take the narrow path", "Climb the rocky slope"]
    choice = make_choice(options)

    if choice == 1:
        print("\nThe narrow path leads to a dead end. You need to turn back.")
        return "game_over"
    else:
        print("\nThe rocky slope is challenging, but you reach the summit and spot the artifact!")
        return "success"

def desert_path():
    print("\nYou trek through a scorching desert. The sun beats down relentlessly.")
    options = ["Search for an oasis", "Continue straight through the dunes"]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou find a hidden oasis, replenish your strength, and continue your journey.")
        print("\nWhile exploring the oasis, you stumble upon the mystical artifact!")
        return "success"
    else:
        print("\nThe endless dunes disorient you, and you get lost. Game over!")
        return "game_over"

def play_game():
    intro()

    print("\nYou have three paths ahead: ")
    options = ["Take the forest path", "Take the mountain path", "Take the desert path"]
    path_choice = make_choice(options)

    if path_choice == 1:
        result = forest_path()
    elif path_choice == 2:
        result = mountain_path()
    else:
        result = desert_path()

    if result == "success":
        print("\nCongratulations! You found the artifact and saved the village!")
    else:
        print("\nGame over. Better luck next time!")

if __name__ == "__main__":
    play_game()
