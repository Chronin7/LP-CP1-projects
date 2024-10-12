
# I have no clue what your code is doing so i just rewrote it (i bacicly just removed the 0 in the return)
def sum_even_numbers(numbers):
	sum = 0
	for x in str(numbers):
		if int(x) % 2 == 0:
			sum += int(x)
		else:
			return 
	return sum
for x in str(123456789):
	print(sum_even_numbers(x))