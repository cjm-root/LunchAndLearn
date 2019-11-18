
def main():
    welcome_message = "Welcome to Hallmarklabs' Lunch and Learn!"
    subject = "Let's talk about your favorite food!"
    question(subject)


# This function asks the user for their name and favorite food
def question(subject):

    print(subject)

    # Asks the user for their questions and assign their response to variable
    user_name = input("What is your name? ")
    favorite_food = input("What is your favorite food? ")

    # Conditional Logic
    if favorite_food == "Chocolate":
        print("Hey " + user_name + ", we both like Chocolate!")
    else:
        print("Oh, Sorry! I don't like " + favorite_food + ", " + user_name)


if __name__ == "__main__":
    main()
