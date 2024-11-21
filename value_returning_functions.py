# Value-returning functions
import random

def getHabitat(animal):
    if animal in ["turtle", "fish", "anemone", "urchin", "jellyfish", "shark"]:
        return "ocean"
    if animal in ["spider", "scorpion", "camel", "iguana", "fox", "snake"]:
        return "desert"
    if animal in ["lemur", "monkey", "tiger", "parrot", "panda", "panther"]:
        return "jungle"
    
def getFriends(habitat, numFriends):
    friends = []
    if habitat == "ocean":
        oceanList = ["turtle", "fish", "anemone", "urchin", "jellyfish", "shark"]
        # Loop run numFriends times
        for i in range(numFriends):
            # Adding a random oceanList item to the friends list
            friends.append(random.choice(oceanList))
        return friends

    if habitat == "desert":
        desertList = ["spider", "scorpion", "camel", "iguana", "fox", "snake"]
        # Loop run numFriends times
        for i in range(numFriends):
            # Adding a random oceanList item to the friends list
            friends.append(random.choice(desertList))
        return friends       

    if habitat == "jungle":
        jungleList = ["lemur", "monkey", "tiger", "parrot", "panda", "panther"]
        # Loop run numFriends times
        for i in range(numFriends):
            # Adding a random oceanList item to the friends list
            friends.append(random.choice(jungleList))
        return friends 


   
# Define main
def main():
    run_again = "yes"
    while run_again.lower() == "yes":
        print("🐍🦁🐻")
        animal = input("Enter your favorite animal: ")
        habitat = getHabitat(animal.lower())
        print(f"{animal} lives in the {habitat}")
        print()
        numFriends = int(input(f"How many friends for the {animal}? "))
        # Call friend function
        friendsList = getFriends(habitat, numFriends)
        print(f"The animal has the following friends: ")
        # Loop to display all items in friendsList
        for i in friendsList:
            print(i)
        print()
        
        run_again = input("Type 'yes' to run again or 'no' to exit: ")

        

# Call the main
if __name__ == "__main__":
    main()
