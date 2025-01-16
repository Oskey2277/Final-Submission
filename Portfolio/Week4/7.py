number = int(input("Enter the number for the times table (negative for reverse): "))
if -12 <= number <= 12:
    if number < 0:
        number = abs(number)
        for i in range(12, -1, -1):
            print(f"{i} x {number} = {i * number}")
    else:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
else:
    print("Error: Number must be between -12 and 12.")