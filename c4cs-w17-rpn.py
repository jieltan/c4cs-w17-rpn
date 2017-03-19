#!/usr/bin/env python3

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2
import operator

OPERATORS = {
	'+': add,
	'-': subtract,
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}

