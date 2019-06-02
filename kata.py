import sys

def calAdd(*argv):
    total = 0

    for arg in argv:
		total = total + int(arg.strip() or 0)

    return total