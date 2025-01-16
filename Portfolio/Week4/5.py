def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    temp_input = input("Enter temperature (e.g., 25C or 77F): ").strip()
    if temp_input[-1].upper() == 'C':
        celsius = float(temp_input[:-1])
        print(f"{celsius}C is {celsius_to_fahrenheit(celsius):.2f}F")
    elif temp_input[-1].upper() == 'F':
        fahrenheit = float(temp_input[:-1])
        print(f"{fahrenheit}F is {fahrenheit_to_celsius(fahrenheit):.2f}C")
    else:
        print("Invalid temperature format.")