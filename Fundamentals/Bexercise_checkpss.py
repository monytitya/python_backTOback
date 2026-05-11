# check password

username = "admin"
password = "123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login Successful!")
elif input_username == username and input_password != password:
    print("Wrong Password!")
else:
    print("Access Denied!")
