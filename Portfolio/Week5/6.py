
if __name__ == "__main__":
    temps = []
    for _ in range(6):
        temp_input = input("Enter temperature (e.g., 25C): ").strip()
        if temp_input[-1].upper() == 'C':
            temps.append(float(temp_input[:-1]))
        else:
            print("Invalid format, try again.")

    if temps:
        print(f"Max: {max(temps):.2f}C, Min: {min(temps):.2f}C, Mean: {sum(temps)/len(temps):.2f}C")
    else:
        print("No temperatures entered.")


