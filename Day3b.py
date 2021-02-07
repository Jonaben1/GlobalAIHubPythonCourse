#login system with using dictionaries
print("****login****")

login = {"userEmail": "lambda@test.com", "userPassword": "lambda"}

logEmail = input("Please enter your email:")
logPassword = input("Please enter your pasword:")


if (login["userEmail"] != logEmail and login["userPassword"] != logPassword):
    print("Invalid email and password.")
elif (login["userEmail"] != logEmail and login["userPassword"] == logPassword):
    print("Invalid email.")
elif (login["userEmail"] == logEmail and login["userPassword"] != logPassword):
    print("Invalid password")
else:
    print("Logged in successfully.")