#!/usr/bin/env python
#
# this file is for implementing value iteration algorihtm
# in this file, we encode save as 1, delete as 2 ans ask as 3

import sys
from collections import defaultdict
import matplotlib.pyplot as plt

from init import initialization
from prune import pruning
from value_iter import value_iter

def check_argv():
	if len(sys.argv) > 1:
		sys.stderr.write("WARNING: file wrongly called! this file"
							"do not need any arguments\n")

def plot(values):
	"""
	Plot the optimal values of each actions with different color
	:param values: dict{list[list[value(s1), value(s2), ...]]}
	"""
	colors = ['green', 'blue', 'red', 'green', 'brown', 'blacky']
	for act in values:
		for value in values[act]:
			plt.plot(value, color=colors[int(act) - 1])
	plt.show()

def main():
	# check input format
	check_argv()

	# set parameters
	p_tran, p_obsv, reward = initialization()
	T = 2  # iteration number

	# value iteration
	values = value_iter(p_tran, p_obsv, reward, T)
	print values

	# plot
	plot(values)

if __name__ == "__main__":
	main()