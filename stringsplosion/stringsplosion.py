class StringSplosion(object):
	def __init__(self, string):
		self.string = string

	def __str__(self):
		return self.string

	def manipulate(self):
		# for i in range(len(self.string) + 1):
		# 	print(self.string[:i], end = '')
		lst = self.string[:1].split()
		while True:
			for i in range(2,len(self.string) + 1):
				lst.append(self.string[:i])
			lst = ''.join(lst)
			return lst
		
			
# string_splosion = StringSplosion('Code')
# print(string_splosion.manipulate())
# string_splosion = StringSplosion('abc')
# print(string_splosion.manipulate())
# string_splosion = StringSplosion('andela')
# print(string_splosion.manipulate())
