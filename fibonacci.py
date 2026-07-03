def fibonacci(n):
	a, b, counter = 0, 1, 0
	while(counter < n):
		yield a
		a, b = b, a+b
		counter += 1

generator = fibonacci(10)
for i in generator:
	print(i, end=' ')
print('')
