
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}C is {celsius_to_fahrenheit(celsius):.2f}F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}F is {fahrenheit_to_celsius(fahrenheit):.2f}C")

