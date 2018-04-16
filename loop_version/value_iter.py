#!/usr/bin/env python
#

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
    :rypte:            dict[list[list[v(s1), v(s2)]]]
  """

  # initialize optimal values in the previous step
  values_pre = {"":[[0 for _ in state_set]]}

  for _ in range(T):
    # # generate {v^{a,k}}, values of all possibly useful CPs
    values = [val for act in values_pre for val in values_pre[act]]
    # # generate K = {values}^{|obsv_set|}
    K = []
    for val1 in values:
      for val2 in values:
        K.append([val1, val2])

    # # compute the values in the current layer
    values_new = defaultdict(list)
    for act in action_set:
      for value_pre in K: # corresponding to two observation
        value_new = [0 for i in state_set]
        for s in state_set:
          value_new[int(s)] = reward[s + act]
          for obsv in obsv_set:
            for s_prime in state_set:
              value_new[int(s)] += gama * ( 
                                          p_tran[s_prime + s + act] * 
                                          p_obsv[obsv + s_prime + act] * 
                                          value_pre[int(obsv)][int(s_prime)]
                                          )
        values_new[act].append(value_new)
    
    # # pruning       
    values_pre = pruning(values_new)

  return values_pre