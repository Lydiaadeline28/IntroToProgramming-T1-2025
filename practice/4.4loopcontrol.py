#1. Create a loop that prints numbers from 1 to 20, but use `break` to stop the loop when you reach 15.
#2. Write a program that uses a loop to print only the odd numbers from 1 to 30, utilizing the `continue` statement.
#3. Implement a loop with the `pass` statement in place of a future feature, and explain what the intended feature would be.
#4. Modify a loop that counts down from 10 to 1, skipping the number 5 using the `continue` statement.
#5. Create a program that sums all numbers in a list but stops adding when it encounters a negative number using the `break` statement.
for i in range(1, 21):
    print(i)
    if i== 15:
        break

for i in range(1,31,2):
    if i % 2 == 0: #the percent sign will divide 2 by 0 and give you the remainder
        continue
    print(i)

for i in range(1, 11):
    print(i)
    if i== 7:
        pass #will stop and say something at 7

for i in range(10, 0, -1): #-1 will make it count down
    if i == 5:
        continue  # Skip the number 5
    print(i)
my_list = [1,2,3,4,5,6,7,8,-2]
sum = 0 

for n in my_list:
    if n < 0:
        break
    sum +=n
print(sum)