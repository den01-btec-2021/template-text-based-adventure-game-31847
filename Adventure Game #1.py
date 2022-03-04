def main():
    print ("Welcome to my game!")
    player_name = input("What is your name? ")
    print ("Hi " + player_name)

    life_counter = 3
    print (f"You have {life_counter} remaining lives")
    print ("There are 4 directions you can move. Forward, left, right or backwards")
    direction = input("Which direction do you want to go? ")
    if direction == "forward":
        print("You went forward")
    elif direction == "backwards":
        print("You went backwards")
    elif direction == "left":
        print("You went left")
    elif direction == "right":
        print("you went right")
    else: print ("Sorry, not recognised!")

main()