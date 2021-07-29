
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
num =int(input("enter a number :"))
list=list(range(1,num+1))
divisors=[]

def find_divisors():
	for number in list:
		if num%number==0:
			divisors.append(number)
	print(divisors)
find_divisors()








# Ask the user for a number and determine whether the number is prime or not. 
num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def find_prime(n):
	if num > 1:
		if len(a) == 0:
			print ('prime')
		else:
			print ('not prime')
	else:
		print ('not prime')
	
find_prime(num)

