import random   # importing the random module
import datetime
import os

# function to generate a password.
def generate_Password(n):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    chosenLetter = random.sample(characters, n)
    password = "".join(chosenLetter)
    return password

#check the strength of generated password based on its length.
def check_password_strength(password):
    if len(password) <= 8:
        return "Weak \u2717"
    elif len(password) < 12: 
      return " Moderate" 
    else:
        return "Strong \u2713"  

# functin for storing password history.
def save_password_to_file(password, filename):
    current_time = datetime.datetime.now()
    with open(filename, "a") as file:
        file.writelines([password ,'\t',str(current_time), "\n"])

# functin to read password history.
def read_password_history(filename):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    password_file = "passwords.txt"  # Define the filename
    if not os.path.exists(password_file):
        open(password_file, 'w').close()  # Create the file if it doesn't exist
    while True:
        users_choice = input("Please enter 'generate' if you want to generate a password, 'history' to view saved passwords, or 'exit' to quit: ")
        if users_choice == 'exit':
            break
        elif users_choice == 'generate':
            # Error handling in case of -ve length of password.
            try:
                n = int(input("Enter the length of the password: "))
                qty = int(input("How many passwords do you want:"))
                # minimum length of password is above 8
                if n < 8 or qty <= 0:
                    print(" \u26A0  Password length should be greater than 8 and quantity should be greater than zero.")
                else:
                    while qty > 0:
                        password = generate_Password(n)

                        print("A randomly selected password is:", password)
                       
                        # Save the generated password to a text file
                        save_password_to_file(password, "passwords.txt")

                        qty -= 1
                    strength = check_password_strength(password)
                    print("Password Strength Indicator:", strength )
                    print("Passwords saved to 'passwords.txt'. \u2713 ")
            except ValueError:
                print(" \u26A0 Invalid input. Please enter valid integer values for password length and quantity.")

        elif users_choice == "history" :
            history = read_password_history("passwords.txt")
            if history:
                print("Password History:")
                print(history)
            else:
                print("No password history available.")
        
        else:
            print("\u26A0  Invalid choice. Please enter 'generate', 'history', or 'exit'..")

