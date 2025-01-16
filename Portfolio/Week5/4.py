
def remove_last_char(s):
    return s[:-1] if len(s) > 1 else s


if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Modified string:", remove_last_char(string))