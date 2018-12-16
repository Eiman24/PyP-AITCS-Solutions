# Programming 07
# A program to compute the value of an investment


def main():
    print("This program calculates the future value")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the interest years: "))
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest: "))

    for i in range(years):
        principal = principal + yearlyinvestment
        principal = principal * (1 + apr)

    print("The value in %d years is %f" % (years, principal))


main()
