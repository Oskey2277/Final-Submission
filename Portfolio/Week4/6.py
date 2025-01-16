for i in range(13):
    print(f"{i} x 7 = {i * 7}")


number = int(input("Enter the number for the times table (0-12): "))
if 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Number must be between 0 and 12.")
