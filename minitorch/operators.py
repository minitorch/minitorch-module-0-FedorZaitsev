"""Collection of the core mathematical operators used throughout the code base."""


# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

import math
from typing import Callable, List

def mul(a: float, b: float) -> float:
	""" Multiplication """
	return a * b

def id(a: float) -> float:
	""" Identity """
	return a

def add(a: float, b: float) -> float:
	""" Addition """
	return a + b

def neg(a: float) -> float:
	""" Negation """
	return -a

def lt(a: float, b: float) -> float:
	""" Comparison < """
	return float(a < b)

def eq(a: float, b: float) -> float:
	""" Comparison = """
	return float(a == b)

def max(a: float, b: float) -> float:
	""" Max """
	if a > b:
		return a
	else:
		return b

def is_close(a: float, b: float) -> float:
	""" Comparison close """
	return float(abs(a - b) < 1e-2)

def sigmoid(a: float) -> float:
	""" Sigmoid function """
	if a >= 0:
		return 1.0 / (math.exp(-a) + 1.0)
	else:
		return math.exp(a) / (math.exp(a) + 1.0)

def relu(a: float) -> float:
	""" ReLU """
	return a * (x > 0)

def log(a: float) -> float:
	""" Log a """
	return math.log(a + 1e-7)

def exp(a: float) -> float:
	""" Exponent """
	return math.exp(a)

def log_back(a: float, b: float) -> float:
	""" Log derivative """
	return b / a

def inv(a: float) -> float:
	""" Inversion """
	return 1.0 / a

def inv_back(a: float, b: float) -> float:
	""" Inversion derivative """
	return -b / (a * a)

def relu_back(a: float, b: float) -> float:
	""" ReLU derivative """
	return b * (a > 0)





# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
