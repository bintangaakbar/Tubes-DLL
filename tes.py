# users = {}
# status = ""
# oldUser1 = ["farhan", "bintang", "pro"]
# passwold= [123, 234, 450]
 
# def displayMenu():
#     status = input("Are you registered user? y/n? Press q to quit")
#     if status == "y":
#         oldUser()
#     elif status == "n":
#         newUser()
 
# def newUser():
#     createLogin = input("Create login name: ")
 
#     if createLogin in users:
#         print("\nLogin name already exist!\n")
#     else:
#         createPassw = input("Create password: ")
#         users[createLogin] = createPassw
#         print("\nUser created\n")
 
# def oldUser():
#     login = input("Enter login name: ")
#     passw = input("Enter password: ")
 
#     if login in oldUser1 and users[login] == passwold:
#         print("\nLogin successful!\n")
#     else:
#         print("\nUser doesn't exist or wrong password!\n")
 
# while status != "q":
#     displayMenu()

CorrectUsername = ['Bintang']
CorrectPassword = [123]

loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == CorrectUsername and password == CorrectPassword:
        print ("Logged in successfully ")
        loop = 'false'
    else:
        print ("Username incorrect!")