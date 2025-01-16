# interval_encryption.py
import random
import string

def interval_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = ""
    random_chars = lambda: random.choice(string.ascii_lowercase)
    for char in message:
        encrypted_message += char + "".join(random_chars() for _ in range(interval - 1))
    return encrypted_message, interval

# Test interval_encrypt
if __name__ == "__main__":
    message = input("Enter a message: ").replace(" ", "")
    encrypted_message, interval = interval_encrypt(message)
    print(f"Encrypted message: {encrypted_message}")
    print(f"Interval: {interval}")