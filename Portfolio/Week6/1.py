# binary_representation.py
def to_binary(num):
    return bin(num)[2:]

# Test to_binary
if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print(f"Binary representation: {to_binary(number)}")
