# simple_encryption.py
def simple_encrypt(message):
    return message.replace(" ", "")[::-1]

# Test simple_encrypt
if __name__ == "__main__":
    message = input("Enter a message: ")
    print(f"Encrypted message: {simple_encrypt(message)}")
