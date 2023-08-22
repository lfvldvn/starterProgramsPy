import random
import string

def password_generate():
    size = 14
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(size))
    return password

def main():
    choice = input("Do you want to generate a passwrod now? (yes/no): ")

    if choice.lower() == "yes":
        new_password = password_generate()
        print("Your new password is:", new_password)
    elif choice.lower() == "no":
        print("No password generate.")
    else:
        print("Invalide choice.")

if __name__ == "__main__":
    main()
