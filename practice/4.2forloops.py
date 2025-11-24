for i in range(10,0,-1):
    print(i)
my_list= [6,21,54,5,8,9,4,2,34,45]
sum =0
for num in my_list:
    sum= sum+sum
print(sum)

small_list = [1,1,3,2,2,5,4,4,2,5]
sqaured_list=[]
for num in small_list:
    sqaured_list.append(num*num)
    print(sqaured_list)
my_string= input("Enter a word\n>")
num_vowels=0
for char in my_string:
    if char in ["a", "e", "i", "o", "u"]:
        num_vowels+=1
print(num_vowels)

user_num = input("Enter an integer")

try:
    user_num = int(user_num)
except:
    print("not an integer...")
for i in range(1,10):
    print(str(user_num) +"x" + str(i) + "=" + str(user_num*i))