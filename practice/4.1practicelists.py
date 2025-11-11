fav_food =["Chicken satay","birria tacos","dumplings"]
fav_candy=["Kinder beuno","Albanese gummy bears","sour patch" ]
cool_drugs=[]

fav_food.append("ice cream") #adds index to end of list
fav_food.insert(1, "Pizza") # adds index at position
fav_food.extend(fav_candy) # list to end of list
fav_candy.remove("Kinder beuno") # removes occerence of the first value
fav_candy.pop(1) #removes specific index
fav_candy.clear #removes every item
fav_candy.sort() 

print(fav_food[1])
print(fav_food)