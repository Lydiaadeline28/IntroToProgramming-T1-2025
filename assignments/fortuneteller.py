def fortune_teller ():
    print("FORTUNE TELLING: IN WHAT YEAR WILL YOU GET RICH?")

    try:
        num_1 = int(input("Enter your lucky number\n>"))
        
    except: 
        print("you must enter an integer")
        fortune_teller()
    
    try:
        num_2 = float(input("Enter how many years(float) into the future you wish to see\n>"))
        
    except:
        print("you must enter a float")
        fortune_teller()
    try:
        num_3 = float(input("Enter a magical float to finally determine your fate\n>"))
        
    except:
        print("you must enter a float")
        fortune_teller()
    
    
    import random
    random_1 = random.randint(1, 10) # Generates a random integer between 1 and 10 (inclusive)
    float(random_1)
    total= num_1 + num_2 + num_3 + random_1
    if total >= 2:
        print("you will be rich in 9 years")
    elif total >= 20:
        print("You will be rich in 56 years")
    elif total >= 100:
        print("You will be rich in 23 years")
    elif total >= 40:
        print("You will be rich in 100 years")
    else:
        print("You will be rich in 92 years")
fortune_teller()