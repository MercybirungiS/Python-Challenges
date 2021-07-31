
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

# 8

def find_divisors(num):
	divisors=[]
	list=(range(1,num+1))
	for number in list:
		if num%number==0:
			divisors.append(number)
	print(divisors)
find_divisors(5)
find_divisors(123)
find_divisors(90)







# Ask the user for a number and determine whether the number is prime or not. 



def find_prime(num):
	a = [x for x in range(2, num) if num % x == 0]
	if num > 1:
		if len(a) == 0:
			print ('prime')
		else:
			print ('not prime')
	else:
		print ('not prime')
	
find_prime(7)
find_prime(345)
find_prime(9)
find_prime(80)


