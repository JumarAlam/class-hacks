def decimal_to_base_n(number, base, \
	symbolarray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):

	if(base > len(symbolarray)):
		raise ValueError

	result = ''
	number = int(number)
	i = 0

	print "%d | %d" % (base, number)

	if(number == 0):
		print 0
		exit()

	while(number != 0):
		remains = number % base
		number = number / base
		i += 1
		print "%s%d | %d - %d" % (" "*i, base, number, remains)
		result += symbolarray[remains]

	print result[::-1]

def base_n_to_decimal(number, base, \
	symbolarray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):

	if(base > len(symbolarray)):
		raise ValueError

	result = 0
	number = str(number)

	for i in range(0, len(number)):
		intermediate = (base**i)*int(number[-i-1])
		print "%s * %d^%d = %d" % (number[-i-1], base, i, intermediate)
		result += intermediate

	print result

