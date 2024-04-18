import sys

def mm_to_point(x):
	return x * 2.83465

def point_to_mm(x):
	return x * 0.352778


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

