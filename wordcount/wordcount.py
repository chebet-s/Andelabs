def words(string):
	x = {}
	word_list = string.split()
	for word in word_list:
		if word.isdigit():
			word = int(word)
		if word in x:
			x[word] = x[word] + 1
		else:
			x[word] = 1
	return x


# print(words('word'))
# print(words("one of each"))
# print(words("one fish two fish red fish blue fish"))
# print(words('car : carpet as java : javascript!!&@$%^&'))
# print(words('testing 1 2 testing'))
# print(words('go Go GO'))
# print(words('¡Hola! ¿Qué tal? Привет!'))
# print(words('hello\nworld'))
# print(words('hello\tworld'))
# print(words('hello  world'))