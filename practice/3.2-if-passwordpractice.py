def check_password():
    real_password = "strawberry25"
    sumbitted_password = input ("Enter password:")

    if real_password == sumbitted_password:
        print("access granted")

    else:
        print("access denied")
        check_password() # runs the function again 
check_password()
