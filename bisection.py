# Program to find the root for a function using bisection method.
# Mohammad Albrahim 2022

import math

def inputFunction(prompt):
	expression = input(prompt)
	if expression == "":
		expression = "x**3 - 2*x - 5"
		print(f'No expression entered. f(x) = {expression} will be used.')
	
	return lambda x: eval(expression, {}, {"x": x})

f = inputFunction('Enter python expression: f(x) = ')
a = float(input('Enter value a: '))
b = float(input('Enter value b: '))
maxIterations = float(input('Enter the number of iterations: '))

if a > b:
	print('invalid range')
	exit()

if not f(a)*f(b) < 0:
	print(f'f(x) has no root in ({a}, {b})')
	exit()

def bisection(f, an, bn, i=1, maxIterations=5):
	cn = (an+bn)/2
	sign = int(math.copysign(1, f(cn)))
	
	if i == 1: print(f'i\tan\tbn\tcn\tsign')
	print(f'{i}\t{round(an, 4)}\t{round(bn, 4)}\t{round(cn, 4)}\t{sign}')
	
	if i == maxIterations:
		return cn
	else:
		nextAn = cn if sign < 0 else an
		nextBn = cn if sign > 0 else bn
		nextI = i + 1
		return bisection(f, nextAn, nextBn, nextI, maxIterations)
	

root = bisection(f, a, b, maxIterations=maxIterations)
print(f'the root for f(x) is {root}')