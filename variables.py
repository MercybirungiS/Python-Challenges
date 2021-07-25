num =int(input("Enter a number: "))
check=int (input("Enter a number to divide by : "))
if num % 4 ==0:
    print(num,"is divisable by 4")
elif num % 2==0:
    print(num,"is even")
else:
    print(num,"is odd")

if num % check==0:
    print (num,"divides evenly by ", check)
else :
    print(num,"doesn't divide evenly by",check)

# grade = int(input("Enter your grade: "))
# if grade >= 90:
#   print("A")
# elif grade >= 80:
#   print("B")
# elif grade >= 70:
#   print("C")
# elif grade >= 65:
#   print("D")
# else:
#   print("F")
