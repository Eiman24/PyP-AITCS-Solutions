# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter the first number between 0 and 1:"))
    y = eval(input("Enter the second number between 0 and 1:"))
    print("input    {0}          {1}".format(x, y))
    print("---------------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("       {0:0>7.6f}      {1:0>7.6f}".format(x, y))

main()