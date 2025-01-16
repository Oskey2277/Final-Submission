
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


if __name__ == "__main__":
    string = input("Enter a string: ")
    uppercase, lowercase = count_case(string)
    print(f"Uppercase letters: {uppercase}, Lowercase letters: {lowercase}")
