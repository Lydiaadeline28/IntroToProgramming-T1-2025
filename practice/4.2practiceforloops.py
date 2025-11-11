#games = ["block blast", "roblox","Fishdom" ]
#for game in games:
    #print(game)
    #print("Number" + game)

#numbers=[1,2,3,4,5]
#for num in numbers:
   # print(num)
#for i in range (0,3):
# first number "0" is included but the last number is not included "3" so it will only print 3 numbers (0,1,2,3)
    #print("Rank" + str(i)+ ":" + games[i])
#print every odd number in loop
#for i in range(1,100,2):
    #print(i)
#create a list of 100 numbers from -100 to 100
#print ony positive numbers 

import random 
random_numbers = []
for i in range (0,100):
    random_numbers.append(random.randint(-100,101))
for num in random_numbers:
    if num >(): 
        print(num)
for i in range (0, len(random_numbers)):
    if random_numbers [i]< 0:
        random_numbers.pop(i)
print(random_numbers)

