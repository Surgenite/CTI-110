# Dylan Makombe
# 11/26/2024
# P5HW
# Using functions to create a game

def create_character():

    name = input("Enter character name: ")
    health = int(input("Enter {name}'s health: "))
    inventory = []
    weapons = ["dagger"]
    strength = int(input("Enter {name}'s strength: "))

    
    character = {
        "Name":name,
        "Health":health,
        "Items":inventory,
        "Weapons":weapons,
        "Strengtg": strength
        }
    return character




def main():
    print("Game is starting...")
    print()
    # Call create character
    char1 = create_character()
    print()
    print(char1)

# Call main
if __name__ == "__main__":
    main()
