# interval_decryption.py
def interval_decrypt(encrypted_message, interval):
    return encrypted_message[::interval]

# Test interval_decrypt
if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    interval = int(input("Enter the interval: "))
    print(f"Decrypted message: {interval_decrypt(encrypted_message, interval)}")
