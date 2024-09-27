
import time


def if_prime():
	no_stopping = True
	prime_list = []
	num = 1
	numb = 0
	while no_stopping == True:
		num += 1
		is_prime = True
		for prime in prime_list:
			if num%prime == 0:
				is_prime = False
				break
		if is_prime == True:
			prime_list.append(num)
			numb += 1
			print(f"{len(prime_list)}: {num}")
			if numb == 100000:
				quit()






print("HI")
if_prime()
time.sleep(10000)
print("your still here")




