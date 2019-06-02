import sys

def calAdd(numString):
    total = 0

    numString = numString.replace('\n', ',')
    numInput = [x.strip() for x in numString.split(',')]
	
    for num in numInput:
		total = total + int(num.strip() or 0)

    return total