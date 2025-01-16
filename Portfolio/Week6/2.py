# integer_factors.py
def factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# Test factors
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(f"Factors: {factors(number)}")
