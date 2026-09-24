# Password Strength Checker

def check_password(password):
    try:
        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters.")

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        special_characters = "!@#$%^&*()-_=+[]{};:',.<>?/"

        for character in password:

            if character.isupper():
                has_upper = True

            elif character.islower():
                has_lower = True

            elif character.isdigit():
                has_digit = True

            elif character in special_characters:
                has_special = True

        if not has_upper:
            raise ValueError("Password must contain an uppercase letter.")

        if not has_lower:
            raise ValueError("Password must contain a lowercase letter.")

        if not has_digit:
            raise ValueError("Password must contain a number.")

        if not has_special:
            raise ValueError("Password must contain a special character.")

        print("Password is Strong.")

    except ValueError as error:
        print("Invalid Password:", error)

    except Exception as error:
        print("Unexpected error:", error)


# Main program
try:
    password = input("Enter your password: ")

    if password.strip() == "":
        raise ValueError("Password cannot be empty.")

    check_password(password)

except ValueError as error:
    print("Error:", error)

