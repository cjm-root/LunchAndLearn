
# Variables and control flow
def main():

    # Variable to store string
    welcome = "Hello NBA!"

    print(welcome)

    # String Variable
    player_name = "James Harden"

    # Numerical Variables
    rebounds = 5
    passes = 10

    player_name_lakers = "LeBron James"
    lebron_r = 10
    lebron_p = 20

    # Start Calculations

    # Integer
    total_rebounds_passes = rebounds + passes

    # Double? / Float / Decimal
    pct_rebounds_passes = rebounds/passes

    # Display to screen
    print("Player " + player_name + " had " + str(rebounds) + " today!")

    # Another Display to screen
    print("Total Rebounds and Passes: ", total_rebounds_passes)
    print("Percentage: ", pct_rebounds_passes)

    # Control flow
    # Decision Making
    if rebounds < lebron_r :
        print("Well Done " + player_name + " !")


if __name__ == "__main__":
    main()
