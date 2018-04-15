#!/usr/bin/env python
#
from collections import defaultdict

def pruning(values_input, optimize_method="sample"):
	"""
	Select only useful and optimal value of plan.
	:para optimize_method: choose methods to do the pruning
	:type input: 		   dict{list[list[v(s1), v(s2)]]}
	:rtype: 			   dict{list[list[v(s1), v(s2)]]}
	"""
	
	values = [val for act in values_input for val in values_input[act]]
	values.sort(reverse=True)

	if optimize_method == "crossing":
		######### accurate way
		optimal= [values[0]]
		y1_max = max(val[1] for val in values)
		target = values[0]
		b_pre  = 0
		i_pre  = 0
		while target[1] != y1_max:
			b_min = 1
			i_min = 0
			for i in range(i_pre + 1, len(values)):
				if values[i][0] - target[0] + target[1] - values[i][1] != 0:
					# the b value of the crossing according to y1 and y0
					b_cross = (values[i][0] - target[0]) / \
							  (values[i][0] - target[0] + target[1] - values[i][1])
					if 0 <= b_cross <= 1 and b_cross > b_pre and b_cross < b_min:
						b_min = b_cross
						i_min = i
			b_pre = b_min
			i_pre = i_min
			target = values[i_min]
			optimal.append(target)

	elif optimize_method == "sample":
	###########sampling way
		optimal = []
		sample  = 160
		for i in range(sample + 1):
			x = i / float(sample)
			max_val = (values[0][1] - values[0][0]) * x + values[0][0]
			max_poi = values[0]
			for value in values:
				val = (value[1] - value[0]) * x + value[0]
				if val > max_val:
					max_val = val
					max_poi = value
			if max_poi not in optimal:
				optimal.append(max_poi)

	# # In case you may want check which action the value is for.
	optimal_dict = defaultdict(list)
	for value in optimal:
		for act in values_input:
			if value in values_input[act]:
				optimal_dict[act].append(value)

	return optimal_dict