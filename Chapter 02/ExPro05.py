# Programming 05
# A program to convert Celsius temps to Fahrenheit


def main():
    for i in range(11):
        celsius = i * 10
        fahrenheit = 9 / 5 * celsius + 32
        i += 1
        print("Celsius:", celsius, "Fahrenheit:", fahrenheit)


main()
