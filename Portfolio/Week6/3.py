# prime_check.py
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test is_prime
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(f"Is prime: {is_prime(number)}")

