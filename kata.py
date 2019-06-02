import sys

def calAdd(numString):
    total = 0
    delim = ','
	
    isDelim = numString[:2]
    if isDelim == '//':
        delim = numString[2:3]
        numString = numString.split('\n')[1]

    numString = numString.replace('\n', delim)
    numInput = [x.strip() for x in numString.split(delim)]

    for num in numInput:
		total = total + int(num.strip() or 0)

    return total