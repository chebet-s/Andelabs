def fizz_buzz(n):
	'''return fizz when divisible by three
	return buzz when divisible by 5
	return fizzbuzz when divisible by both three and five
	'''
	if n % 3 == 0 and n % 5 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n % 5 == 0:
		return 'Buzz'
	else: 
		return n

# print(fizz_buzz(3))
# print(fizz_buzz(33))
# print(fizz_buzz(5))
# print(fizz_buzz(25))
# print(fizz_buzz(15))
# print(fizz_buzz(105))
# print(fizz_buzz(101))
# print(fizz_buzz(8))
