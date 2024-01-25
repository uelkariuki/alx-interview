#!/usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
	"""
	Rotates a 2D matrix 90 degrees clockwise
	"""
	matrix[:] = list(zip(*matrix[::-1]))
