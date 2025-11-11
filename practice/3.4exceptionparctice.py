def times_two ():
    num = input("Enter a number\n>")

    try:
        print(int(num) *2)
    except:
        print("you must enter an integer")
        times_two()

times_two()
