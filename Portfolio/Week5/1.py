
def validate_integer(num):
    return 0 <= num <= 100


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print("In range 0-100:", validate_integer(number))

