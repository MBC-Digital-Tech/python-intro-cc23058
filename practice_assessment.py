print("Welcome to the Dog Breed Selector!")
name = input("What is your name? ")
print("Available dog breeds:")
breeds_list = [" ", "Labrador", "German Shepherd","Beagle","Bulldog", "Poodle"]

for breeds in breeds_list:
    print(breeds)
breeds = int(input("Enter the number of your prefferred dog breed: "))
age = int(input ("Enter the preffered age of dog (1-15):"))
print(f'Thank you, {name}!')
print(f'You prefer {breeds_list[breeds]} that is about {age} years old.')
print("Good luck finding your perfect furry friend!")

if breeds > 5:
    print('Invalid selection please select a number between 1-5')
if age > 15:
    print("Invalid age please select a number between 1-15")
elif age < 1:
    print("Invalid age please select a valid age")