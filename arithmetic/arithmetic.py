def arith_geo(nums):
	# n is the index
	n = 0
	while nums:
		n += 1
		# checking difference to be equal
		if nums[n + 1] - nums[n] == nums[n + 2] - nums[n + 1]:
			return "Arithmetic"
		# checking quotient to be equal
		elif nums[n + 1] / nums[n] == nums[n + 2] / nums[n + 1]:
			return "Geometric"
		# checking both difference to be unequal and quotient to be unequal
		elif nums[n + 1] - nums[n] != nums[n + 2] - nums[n + 1] and nums[n + 1] / nums[n] != nums[n + 2] / nums[n + 1]:
			return -1
	else:
		# checking empty array
		if nums == []:
			return 0



# x = [0.5, 3.5, 24.5, 171.5]
# print(arith_geo(x))
# y = [5, 11, 17, 23, 29, 35, 41]
# print(arith_geo(y))
# z = [1, 2, 3, 5, 8]
# print(arith_geo(z))
# a = []
# print(arith_geo(a))

# print()

# b = [-128, 64, -32, 16, -8]
# print(arith_geo(b))
# c = [15, 10, 5, 0, -5, -10]
# print(arith_geo(c))
# d = [-1, -8, -27, -64, -125]
# print(arith_geo(d))
# e = []
# print(arith_geo(e))