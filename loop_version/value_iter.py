#!/usr/bin/env python
#

from collections import defaultdict
from prune import pruning


def value_iter(p_tran, p_obsv, reward, T):
	"""
	Main function of value iteration
	Args:
		:param p_tran: transition probability P(s'|s,a)
		:param p_obsv: observation probability P(o'|s', a)
		:param reward: rewards r(s, a)
		:param T:	   iteration number
	Return:
		a dictionary with actions as keys and corresponding list of 
		pruned, optimal values of plan as dictionary values 
		:rypte:		   dict[list[list[v(s1), v(s2)]]]
	"""

	# initialization
	gama = 0.95
	action_set = ("1", "2", "3")
	state_set  = ("1", "2")
	obsv_set   = ("1", "2")

	# values = [[0 for _ in state_set]]
	values_pre = {"":[[0 for _ in state_set]]}

	for _ in range(T):
		# # generate {v^{a,k}}, values of all possibly useful CPs
		K = [val for act in values_pre for val in values_pre[act]]
		# # compute the values in the current layer
		values_new = defaultdict(list)
		# for action in ("dosave", "dodelete", "ask"):
		for action in action_set:
			for val1 in K:
				for val2 in K:
					value = [val1, val2]

					# for observation in ("save", "delete"):
					value_new = [0 for i in state_set]	
					# for current state s in ("save", "delete")
					for s in state_set:
						value_new[int(s)-1] = reward[s + action]
						for obsv in obsv_set:
							for s_prime in state_set:
								value_new[int(s)-1] += gama * ( 
													   p_tran[s_prime + s + action] * 
													   p_obsv[obsv + s_prime + action] * 
													   value[int(obsv)-1][int(s_prime)-1]
													   )
					values_new[action].append(value_new)
		values_pre = pruning(values_new)

	return values_pre