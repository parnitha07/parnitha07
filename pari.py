def start_game():
    print("Welcome to the Dungeon Adventure!")
    print("You are about to enter a dark and mysterious dungeon.")
    print("You have two choices: Go Left or Go Right.")
    
    choice = input("Do you choose Left or Right? ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice! Please choose Left or Right.")
        start_game()

def left_path():
    print("\nYou head down the left path and find a dark room.")
    print("In the room, there is a treasure chest and a sleeping dragon.")
    choice = input("Do you open the chest or try to sneak past the dragon? ").lower()

    if choice == "open the chest":
        open_chest()
    elif choice == "sneak past the dragon":
        sneak_past_dragon()
    else:
        print("Invalid choice! Please choose 'open the chest' or 'sneak past the dragon'.")
        left_path()

def open_chest():
    print("\nYou carefully open the chest...")
    print("Inside, you find a pile of gold coins and a magical sword!")
    print("Congratulations! You have become rich and powerful.")
    play_again()

def sneak_past_dragon():
    print("\nYou try to sneak past the dragon...")
    print("Unfortunately, the dragon wakes up and sees you!")
    print("You try to run, but the dragon catches you and you are defeated.")
    play_again()

def right_path():
    print("\nYou head down the right path and encounter a giant spider!")
    print("The spider looks hungry and ready to attack!")
    choice = input("Do you fight the spider or run away? ").lower()

    if choice == "fight":
        fight_spider()
    elif choice == "run away":
        run_away()
    else:
        print("Invalid choice! Please choose 'fight' or 'run away'.")
        right_path()

def fight_spider():
    print("\nYou bravely fight the spider and after a tough battle, you defeat it!")
    print("The path ahead is now clear.")
    print("You continue exploring the dungeon, finding more treasures along the way.")
    play_again()

def run_away():
    print("\nYou turn around and run as fast as you can...")
    print("But the spider catches you in its web!")
    print("You try to escape, but it’s too late. You are trapped.")
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (yes/no): ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid choice! Please type 'yes' or 'no'.")
        play_again()

# Start the game
start_game()
