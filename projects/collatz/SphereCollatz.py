#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------


#!/usr/bin/env python3

import sys

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
	"""
	read two ints
	s a string
	return a list of two ints, representing the beginning and end of a range, [i, j]
	"""
	a = s.split()
	return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def cycle_length (n) :
	assert n > 0
	c = 1
	while n > 1:
		if (n % 2) == 0 :
			n = (n // 2)
		else :
			n = (3 * n) + 1
		c += 1
	assert c > 0
	return c

def collatz_eval (i, j) :

	"""
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	return the max cycle length of the range [i, j]
	"""
	# <your code>
	if (i > j) :
		temp = i
		i = j
		j = temp
	# range should be within 0 to 1,000,000
	assert i > 0
	assert j < 1000000
	max = 0
	for n in range (i, j + 1):
		c = cycle_length(n)
		if (c > max) :
			max = c
	assert c > 0
	return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
	"""
	print three ints
	w a writer
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	v the max cycle length
	"""
	w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
	"""
	r a reader
	w a writer
	"""
	for s in r :
		i, j = collatz_read(s)
		v    = collatz_eval(i, j)
		collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__" :
	collatz_solve(sys.stdin, sys.stdout)