# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account 
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance= int(input("Set your savings balance."))
    print(f"Your saving balance is {savings_balance}")

    savings_interest= int(input("Set your interest rate."))
    print(f"Your interest rate is {savings_interest}")

    savings_maturity= int(input("Set the amount of months you are saving your balance."))
    print(f"Your money in savings for this amount of months: {savings_maturity}")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, calculated_interest_earned =create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned is {calculated_interest_earned}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance=int(input("Set you CD balance"))
    cd_interest=int(input("Set your interest rate"))
    cd_maturity=int(input("Set the amount of months"))
    # Call the create_cd_account function and pass the variables from the user.
    create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"You earned {calculated_interest_earned} and your updated balance in your cd account is :{updated_savings_balance} for the given {cd_maturity} months")

if __name__ == "__main__":
    # Call the main function.
    main()
