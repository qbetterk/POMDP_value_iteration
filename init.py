#!/usr/bin/env python
#

def initialization():
	"""

	"""
	# # Transition function P(s'|s,a)
	p_tran = {}
	# s' is "save" and a is not "ask"
	p_tran["111"] = p_tran["112"] = p_tran["121"] = p_tran["122"] = 0.65
	# s' is "delete" and a is not "ask"
	p_tran["211"] = p_tran["212"] = p_tran["221"] = p_tran["222"] = 0.35
	# a is "ask"
	p_tran["113"] = p_tran["223"] = 1.0
	p_tran["213"] = p_tran["123"] = 0.0

	# # Observation function P(o'|s', a)
	p_obsv = {}
	# a is "ask"
	p_obsv["113"] = 0.8 ; p_obsv["213"] = 0.2
	p_obsv["123"] = 0.3 ; p_obsv["223"] = 0.7
	# a is not "ask", observation gives no useful information
	for i in [1,2]:
		for j in [1,2]:
			for k in [1,2]:
				p_obsv[str(i)+str(j)+str(k)] = 0.5

	# # reward function r(s, a)
	reward = {}
	# case of "asking"
	reward["13"] = -1
	reward["23"] = -1
	# case of correct action
	reward["11"] = 5
	reward["22"] = 5
	# case of wrong action
	reward["12"] = -20
	reward["21"] = -10
	
	return p_tran, p_obsv, reward