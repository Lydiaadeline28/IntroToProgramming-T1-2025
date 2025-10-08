def check_password():
    real_answer = "blue"
    sumbitted_answer = input ("what color is the sea?:") 

    if real_answer == sumbitted_answer:
        print("correct")

    else:
        print("incorrect")
    real_answer = "yellow"
    sumbitted_answer = input ("what color are bananas?:") 

    if real_answer == sumbitted_answer:
        print("access granted")

    else:
        print("incorrect")
    real_answer = "orange"
    sumbitted_answer = input ("What color is an orange?:") 

    if real_answer == sumbitted_answer:
        print("access granted")

    else:
        print("incorrect")
       
check_password()