# Programming 04
# A program to convert Celsius temps to Fahrenheit


def main():
    celsius = eval(input("Input a Celsius temperature: "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


for i in range(5):
    main()
