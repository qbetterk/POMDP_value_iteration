#!/usr/bin/env python
#
import sys
import matplotlib.pyplot as plt

from init import initialization
from prune import pruning
from value_iter import value_iter

def check_argv():
  """
  check whether input command is in suitable format
  """
  if len(sys.argv) > 1:
    sys.stderr.write("WARNING: file wrongly called! this file"
                       "do not need any arguments\n")

def plot(values):
  """
  Plot the optimal values of each actions with different color
  :param values: dict{list[list[value(s1), value(s2), ...]]}
  """
  
  # # get crossing # #
  dosave     = values["0"][0]
  dodelete   = values["1"][0]
  ask_save   = values["2"][0]
  ask_delete = values["2"][-1]
  cro_left   = (dosave[0] - ask_save[0]) /  \
               (dosave[0] - ask_save[0] + ask_save[1] - dosave[1])
  cro_right  = (dodelete[0] - ask_delete[0]) / \
               (dodelete[0] - ask_delete[0] + ask_delete[1] - dodelete[1])

  # # plot
  colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
  for act in values:
    for value in values[act]:
      plt.plot(value, color=colors[int(act)])
  plt.vlines([cro_left, cro_right], -20, 10, linestyles='dashed', colors='r')
  plt.ylim(-20, 13) 
  plt.xlim(0,   1)
  plt.text(cro_left/2-0.05, 10, r"doSave")
  plt.text((cro_right + cro_left)/2 - 0.02, 10, "ask")
  plt.text((cro_right + 1)/2-0.07, 10, "doDelete")
  plt.show()


def main():
  # # check input format
  check_argv()

  # # set parameters
  state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama = initialization()

  # # set iteration number
  T = 100

  # # value iteration
  values = value_iter(state_set, action_set, p_tran, reward, obsv_set, p_obsv, gama, T)

  # # plot
  plot(values)

if __name__ == "__main__":
  main()