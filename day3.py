# print (10 > 9)
# broughtFood = True
# print(broughtFood)

# is_raining = True
# if is_raining:
#     print("Take an umbrella!")
# else:
#     print("No umbrella needed.")

# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
#     print(message)


name = input("Enter your name:")
while name == "":
    print("You did not enter your name")
    name= input("enter your name")

    age = int(input("Enter your age:"))
    while age < 0:
        print(f"you are (age) years old")

        food = input("enter a food you like")

        while food == "q":
            print(f"You like (food)")
            food = input ("enter your name")

            num = input("enter a number between 1 - 10")
            while our (num) < 1 or num > 10: 
                print (f"(num)"is not valid)
print("your number is (num)")