"""The Python program providing access to different financial calculators."""
import math


def calculate_compound_interest(P, r, t):
    """
    Calculate compound interest using the formula:
    A = P * (1 + r) ** t
    Returns the final amount A.
    """
    return P * math.pow((1 + r), t)

# Allow the user to choose a calculation.


print("Choose which calculation you want to do:")
print(" Investment - to calculate the interest you'll earn on your investment")
print(" Bond - to calculate the amount you'll have to pay on a home loan")

calc = input("Enter either'Investment' or 'Bond' to proceed: ")

if calc == "investment" or calc == "INVESTMENT" or calc == "Investment":
    P = float(input("Enter the amount you are depositing: "))
    i = float(input("Enter the interest rate: "))
    t = float(input("Enter the number of years you plan on investing: "))
    # we divide the number inserted by the user by 100 to get the interest rate
    r = i / 100

    print("Choose the interest: ")
    print("1. Simple interest")
    print("2. Compound interest")
    interest = int(input("Enter the number of your choice: "))
    if interest == 1:
        print("Simple interest")
        # Calculate the amount using the simple interest formula
        A = P * (1 + r * t)
        # Where:
        # A = total amount, 
        # P = principal amount,
        # r = rate of interest, 
        # t = time the money is invested for.
        print("Your investment after {} years will be R{}".format(t, A))
        a = P * (1 + 0.08 * 20)
        # a represent the amount after 20 years
        difference = a - A
        # A represents the amount after the t years.
        print("Your investment in 20 years at 8% will be R{}".format(a))
        print("The difference will be R{}".format(difference))
    elif interest == 2:
        print("Compound interest")
        # Use the new compound interest function
        A = calculate_compound_interest(P, r, t)
        print("Your investment after {} years will be R{}.".format(t, A))
        a = calculate_compound_interest(P, 0.08, 20)
        difference = a - A
        print("Your investment in 20 years at 8% will be R{}".format(a))
        print("The difference will be R{}".format(difference))
    else:
        print("Invalid option!")
elif calc == "bond" or calc == "BOND" or calc == "Bond":
    P = float(input("Enter the present value of the house: "))
    r = float(input("Enter the interest rate: "))
    n = float(input("Enter the number of months you plan to repay the bond: "))
    # We divide the number inserted by the user by 100 to get the interest rate
    i = r / 100
    # Calculate the monthly repayment of the bond using the repayment formula
    repayment = (i * P) / (1 - (1 + i)**(-n))
    print("Your monthly repayment will be R{}" .format(repayment))
else:
    print("Error!")
