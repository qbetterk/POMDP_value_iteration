#!/usr/bin/env python
#
import numpy as np
from collections import defaultdict
from prune import pruning

def value_iter(state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama, T):
  """
  Main function of value iteration
  Args:
    :param T:          iteration number
    :param state_set:  set of states 
    :param action_set: set of actions
    :param p_tran:     transition probability P(s'|s,a) 
    :param reward:     expected reward r(s, a)
    :param observ_set: set of observations
    :param p_obsv:     obervation probability P(o'|s', a)
    :param gama:       discount factor
  Return:
    a dictionary with actions as keys and corresponding list of 
    pruned, optimal values of plan as dictionary values 
    :rypte:            dict[list[np.array([v(s1), v(s2)])]]
  """

  # # initialize optimal values in the previous step
  values_pre = {"":[np.zeros(len(state_set))]}

  for _ in range(T):
    # # generate {v^{a,k}}, values of all possibly useful CPs
    values = [val for act in values_pre for val in values_pre[act]]
    # # generate K = {values}^{|obsv_set|}
    K = []
    for val1 in values:
      for val2 in values:
        K.append(np.matrix([val1, val2]))

    # # compute the values in the current layer
    values_new = defaultdict(list)
    for act in action_set:
      for value_pre in K:
        value_new = p_tran[int(act)] * \
                    np.multiply(
                               p_obsv[int(act)],
                               np.transpose(value_pre)
                               ) * \
                    np.matrix([[1],[1]])

        value_new = gama * np.transpose(value_new) + reward[int(act)]
        values_new[act].append(np.array(value_new)[0])

    # # pruning 
    values_pre = pruning(values_new)

  return values_pre
