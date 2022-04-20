# Program to approximate the derivative for a function on a point using numerical difference.
# Mohammad Albrahim 2022

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

diffAt = float(input('Find difference at f\'(?): '))
if diffAt not in domainList:
	print('Selected number not in x list')
	exit()

def forwardDifference(number, domainList, rangeList):
	numberIndex = domainList.index(number)
	currentY = rangeList[numberIndex]
	nextY = rangeList[numberIndex + 1]
	
	approx = (nextY - currentY) / h
	return approx

def backwardDifference(number, domainList, rangeList):
	numberIndex = domainList.index(number)
	previousY = rangeList[numberIndex - 1]
	currentY = rangeList[numberIndex]
	
	approx = (currentY - previousY) / h
	return approx

def centralDifference(number, domainList, rangeList):
	numberIndex = domainList.index(number)
	previousY = rangeList[numberIndex - 1]
	nextY = rangeList[numberIndex + 1]
	
	approx = (nextY - previousY) / (2*h)
	return approx

approx = None
if diffAt == domainList[0]:
	print('Using forward difference method')
	approx = forwardDifference(diffAt, domainList, rangeList)
elif diffAt == domainList[-1]:
	print('Using backward difference method')
	approx = backwardDifference(diffAt, domainList, rangeList)
else:
	print('Using central difference method')
	approx = centralDifference(diffAt, domainList, rangeList)

approx = round(approx, 4)
print(f'The approximated value of f\'({diffAt}) is {approx}')