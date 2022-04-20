# Program to approximate the integration for a function using composite simpson rule.
# Mohammad Albrahim 2022

def inputFunction(prompt):
	expression = input(prompt)
	if expression == "":
		expression = "x**2"
		print(f'No expression entered. f(x) = {expression} will be used.')
	
	return lambda x: eval(expression, {}, {"x": x})

a = float(input('Enter value a integrate from: '))
b = float(input('Enter value b integrate to: '))
n = int(input('Enter the number of sub-intervals: '))
h = (b-a)/n
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

innerList = rangeList[1:-1]
oddRangeList = [innerList[i] for i in range(len(innerList)) if (i+1) % 2 == 1]
evenRangeList = [innerList[i] for i in range(len(innerList)) if (i+1) % 2 == 0]

approx = round((h/3)*(rangeList[0] + rangeList[-1] + 4*sum(oddRangeList) + 2*sum(evenRangeList)), 4)
print(f'The approximated value is {approx}')