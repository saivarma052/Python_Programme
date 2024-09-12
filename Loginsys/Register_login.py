import os

def register():
    username = input("Enter your username: ")
    # User_data.txt check
    if not os.path.exists("user_data.txt"):
        with open("user_data.txt", "w") as file:
            pass
    #

    with open("user_data.txt", "r") as file:
        for line in file:
            sorted_user, _ = line.strip().split(",")
            if username == sorted_user:
                print("Error: Username already exists! Try different username")
                register()
                return True

    password = input("Enter your password: ")

    with open("user_data.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration Successful!")

    return True


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("user_data.txt", "r") as file:
        for line in file:  # Iterate over each line in the file
            sorted_user, sorted_pass = line.strip().split(",")  # Strip whitespace and split the line by comma
            if username == sorted_user and password == sorted_pass:
                print("Login successful")
                return True
        print("Invalid username and password, Please try again!")
        return False


print("Welcome to Login Screen, Choose an Option:")
print("1. Register")
print("2. Login")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    register()
elif choice == "2":
    if login():
        print("You are now Logged in")
    else:
        print("Failed to login")

else:
    print("Invalid Choice! Plesae enter 1 or 2")