password1 = input("Enter a new password (8-12 characters): ")
password2 = input("Re-enter the password: ")
if password1 == password2 and 8 <= len(password1) <= 12:
    print("Password Set")
else:
    print("Error: Passwords must match and be 8-12 characters long.")