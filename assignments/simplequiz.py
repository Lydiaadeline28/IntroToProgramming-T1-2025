answer_one =  answer_one = (input ("What color is a banana?"))
answer_two=  answer_two = (input ("What color is an orange?"))
answer_three=  answer_three = (input ("What color is crab grass?"))
def simple_quiz():
    score=0
    if answer_one.lower == "yellow": #blue text converts it to lowercase 
        score= score + 1
    if answer_two == "orange":
        score= score+1
    print (str(score))
simple_quiz()

