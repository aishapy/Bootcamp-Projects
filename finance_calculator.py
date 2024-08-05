import math

# the program is asking the user to input what type of financial calculation they would like to make
# it requires from the user; the interest rate, capital amount, time (years or months) or house value
# depending on the input the inteded calculation is made by the program

investment_ = ("Select investment to calculate the amount of interest you'll earn on your investment\n")
print(investment_)

bond_ = ("Select bond to calculate the amount you'll have to pay on a home loan\n")
print(bond_)

user_input_calc = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
if user_input_calc == "investment":
    capital_amount = int(input("Please enter your principle amount."))
    interest_rate = float(input("Please enter your rate of interest."))
    time_in_t = int(input("How long is the repayment for in years"))
    interest_ = input("Would you like to calculate simple or compound interest")
    if interest_ == "simple":
        capital_amount * (1 + interest_rate * time_in_t)
        print("This is how much you'll earn with simple interest")
    elif interest_ == "compound":
        capital_amount * math.pow((1+interest_rate),time_in_t)
        print("This is how much you'll earn with compound interest ")
    elif user_input_calc == "bond":
        house_value = int(input("Please enter the value of your house."))
        interest_rate = float ("Please enter your rate of interest.")
        months_ = int(input("How many months would you like to repay the loan for?"))
        (interest_rate * house_value)/(1- (1 + interest_rate)**(-months_))
    else:
        print("Invalid input, please try again.")


