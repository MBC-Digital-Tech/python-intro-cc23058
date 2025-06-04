# starter program week 3 - perhaps this could be a task

def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Butter Chicken ")
    print("2. Pizza")
    print("3. Butter Chicken Burger")
    # add one more meal here
    print("4. Nandos Chicken and chips")
    # combine the line above and below into one command that accepts an integer instead of a string.
    answer = int(input("Which of these meals is your favourite? (1, 2, 3, or 4) "))
    # adapt the if else block to include the fourth meal and compares integers instead of strings.
    if answer == 1:
        print("Butter Chicken coming up")
    elif answer == 2:
        print("Pizza coming up")
    elif answer == 3:
        print("Butter Chicken  Burger coming up!")
    elif  answer == 4:
        print("Nandos Chicken and  chips coming up!")
    print("Enjoy!")


# add a command to run the function above.
cooking()