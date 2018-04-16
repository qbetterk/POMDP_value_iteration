#!/usr/bin/env python
#
import numpy as np

def initialization():
  """
  This function initializes serval parameters that
  would be used during value iteration.
  Return:
    state_set:  set of states
    action_set: set of actions
    p_tran:     transition probability
    reward:     expected reward
    observ_set: set of observations
    p_obsv:     obervation probability
    gama:       discount factor
  """
  
  # # Transition function P(s'|s,a)
  p_tran     = np.zeros(shape=(3,2,2))
  # action is not "ask"
  p_tran[0] = p_tran[1] = np.matrix([[0.65, 0.35],
                                     [0.65, 0.35]])
  # action is "ask"
  p_tran[2] = np.matrix([[1.0, 0.0],
                         [0.0, 1.0]])

  # # # Observation function P(o'|s', a)
  p_obsv     = np.zeros(shape=(3,2,2))
  # action is not "ask", observation gives no useful information
  p_obsv[0] = p_obsv[1] = np.matrix([[0.5, 0.5],
                                     [0.5, 0.5]])
  # action is "ask"
  p_obsv[2] = np.matrix([[0.8, 0.2],
                         [0.3, 0.7]])

  # # reward function r(s, a)
  reward = np.matrix([[5,   -10],
                      [-20, 5],
                      [-1,  -1]])
  
  gama = 0.95
  action_set = ("0", "1", "2")
  # ("0", "1", "2") correspondingly refers to ("dosave", "dodelete", "ask")
  state_set  = ("0", "1")
  # ("0", "1") correspondingly refers to ("save", "delete")
  obsv_set   = ("0", "1")
  # ("0", "1") correspondingly refers to ("save", "delete")
  
  return state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama
