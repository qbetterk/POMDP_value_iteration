#!/usr/bin/env python
#

def initialization():
  """
  This function initializes serval parameters that
  would be used during value iteration:
  Return:
    state_set:  set of states
    action_set: set of actions
    p_tran:     transition probability; 
    reward:     expected reward
    observ_set: set of observations
    p_obsv:     obervation probability; 
    gama:       discount factor
  """

  # # Transition function P(s'|s,a)
  p_tran = {}
  # s' is "save" and a is not "ask"
  p_tran["000"] = p_tran["001"] = p_tran["010"] = p_tran["011"] = 0.65
  # s' is "delete" and a is not "ask"
  p_tran["100"] = p_tran["101"] = p_tran["110"] = p_tran["111"] = 0.35
  # a is "ask"
  p_tran["002"] = p_tran["112"] = 1.0
  p_tran["102"] = p_tran["012"] = 0.0

  # # Observation function P(o'|s', a)
  p_obsv = {}
  # a is "ask"
  p_obsv["002"] = 0.8 ; p_obsv["102"] = 0.2
  p_obsv["012"] = 0.3 ; p_obsv["112"] = 0.7
  # a is not "ask", observation gives no useful information
  for i in [1,0]:
    for j in [1,0]:
      for k in [1,0]:
        p_obsv[str(i)+str(j)+str(k)] = 0.5

  # # reward function r(s, a)
  reward = {}
  # case of "asking"
  reward["02"] = -1
  reward["12"] = -1
  # case of correct action
  reward["00"] = 5
  reward["11"] = 5
  # case of wrong action
  reward["01"] = -20
  reward["10"] = -10
  
  gama = 0.95
  action_set = ("0", "1", "2")
  # ("0", "1", "2") correspondingly refers to ("dosave", "dodelete", "ask")
  state_set  = ("0", "1")
  # ("0", "1") correspondingly refers to ("save", "delete")
  obsv_set   = ("0", "1")
  # ("0", "1") correspondingly refers to ("save", "delete")
  
  return state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama