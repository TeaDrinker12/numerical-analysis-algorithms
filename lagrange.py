# Program to approximate the value for a function on a point using lagrange interpolation.
# Mohammad Albrahim 2022

from functools import reduce

def inputFunction(prompt):
	expression = input(prompt)
	if expression == "":
		expression = "x**2"
		print(f'No expression entered. f(x) = {expression} will be used.')
	
	return lambda x: eval(expression, {}, {"x": x})

a = float(input('Enter value start: '))
b = float(input('Enter value end: '))
n = int(input('Enter the number of divisions: '))
h = round((b-a)/n, 4)
print(f'h = {h}')

domainList = [round(a + step*h, 4) for step in range(0, n+1)]

print('Do you want to use function expression or enter values directly?')
print('1- Use function expression')
print('2- Enter values directly')
selection = int(input('> '))
if not selection in [1, 2]: raise Exception('Only 1 and 2 allowed')

rangeList = None
if selection == 1:
	f = inputFunction('Enter python expression: f(x) = ')
	rangeList = [round(f(x), 4) for x in domainList]
	print('x\tf(x)')
	for i in range(0, n+1):
		print(f'{domainList[i]}\t{rangeList[i]}')
else:
	print('x\tf(x)')
	rangeList = []
	for i in range(0, n+1):
		rangeList.append(float(input(f'{domainList[i]}\t')))

valAt = float(input('Find value at f(?): '))

def lagrange(x, domainList, rangeList):
	lagrangeDomain = [domainList[:i] + domainList[i+1:] for i in range(len(domainList))]
	
	lagrangeNumerators = [reduce(lambda a, b: a*b, [x-e for e in lagrangeDomain[i]]) for i in range(len(domainList))]
	lagrangeDenominators = [reduce(lambda a, b: a*b, [domainList[i]-e for e in lagrangeDomain[i]]) for i in range(len(domainList))]
	
	lagrangeTerms = [(lagrangeNumerators[i]/lagrangeDenominators[i])*rangeList[i] for i in range(len(domainList))]
	lagrangeApprox = sum(lagrangeTerms)
	
	return lagrangeApprox
	

approx = round(lagrange(valAt, domainList, rangeList), 4)
print(f'The approximated value of f({valAt}) is {approx}')