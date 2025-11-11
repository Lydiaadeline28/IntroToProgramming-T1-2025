lydias_faves = {
    "food": "chicken satay",
    "fruit": "orange",
    "city": "Chicago"
}
print(lydias_faves["fruit"])
#add a new entry 
lydias_faves["game"] = "block blast"

# remove an entry
lydias_faves.pop("city")

for key, value in lydias_faves.items():
    print (key) +":" (str(value))
