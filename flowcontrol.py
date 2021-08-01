
#flow control , the sum of the first ten numbers using while

#using while
=======
#flow control , the sum of the first ten numbers using when 

#using when 

num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of first 10 numbers is:", sum)

#using break
for num in range(10):



    if num >10:
        print ("stop running ")
        break
    print(num)
#using continue

for num in range(8,12):
    if num ==10:
        continue
    else:
        print(num)

#using if else
def user (choice):
    if choice ==1:
        print ("Student")
    elif choice==2:
        print("Admin")
    elif choice ==3:
        print("chef")
    else:
        print ("Wrong entry")
user(1)
user(2)
user(3)
user(6)

#Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for num in list:
    if num >150:
        break
    if num %5==0:
        print(num)

# Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# 1 2 3 4 5 6 

print ("next number pattern")
lastnumber=7
for row in range (1,lastnumber):
    for column in range (1,row +1):
        print(column,end='')
    print("")








