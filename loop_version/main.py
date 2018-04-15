#!/usr/bin/env python
#
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
	colors = ['green', 'blue', 'red', 'green', 'brown', 'black']
	for act in values:
		for value in values[act]:
			plt.plot(value, color=colors[int(act)])
	plt.show()


def main():
	# check input format
	check_argv()

	# set parameters
	state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama = initialization()
	# iteration number
	T = 2

	# value iteration
	values = value_iter(state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama, T)
	print values
	# plot
	plot(values)

if __name__ == "__main__":
	main()