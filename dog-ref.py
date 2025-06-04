print("Welcome to the Dog Breed Selector!")
name = input("What is your name? ")

# Dog breed list
breeds_list = ["Labrador", "German Shepherd", "Beagle", "Bulldog", "Poodle"]

# Display breed options
print("Available dog breeds:")
for i, breed in enumerate(breeds_list, start=1):
    print(f"{i}. {breed}")

# Loop until valid breed number is entered
while True:
    try:
        breed_choice = int(input("Enter the number of your preferred dog breed (1-5): "))
        if 1 <= breed_choice <= len(breeds_list):
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a valid number.")

# Loop until valid age is entered
while True:
    try:
        age = int(input("Enter the preferred age of the dog (1-15): "))
        if 1 <= age <= 15:
            break
        else:
            print("Invalid age. Please enter a number between 1 and 15.")
    except ValueError:
        print("Please enter a valid number.")

# Final message
print(f"\nThank you, {name}!")
print(f"You prefer a {breeds_list[breed_choice - 1]} that is about {age} years old.")
print("Good luck finding your perfect furry friend!")
