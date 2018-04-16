#!/usr/bin/env python
#
from collections import defaultdict

def pruning(values_input, optimize_method="sample"):
  """
  Select only useful and optimal value of plan.
  Args:
    :param values_input:    dictionary of values of different actions
    :param optimize_method: choose methods to do the pruning
    :intput type:           dict{list[np.array([v(s1), v(s2)])]}
  Return:
    optimal_dict:           dictionary of pruned values of each action
    :rtype:                 dict{list[np.array([v(s1), v(s2)])]}
  """
  
  values = [val for act in values_input for val in values_input[act]]
  values.sort(key=lambda x:x[0], reverse=True)

  if optimize_method == "crossing":
    """ 
    Accurate method
    This method takes the plan which has the biggest value at b=(1,0)
    as the first target. Then find the crossing on this line whose b is 
    the closest to the (1,0), and take this line(plan) as the second 
    target. In this way, find all the line(plan) which contribute to the 
    upper surface.
    This method could find all the optimal policies, but would be slow
    and even explore when |{V^{n}_{t-1}(s)}| is large.
    """
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
    """
    Sampling method
    This method sets n (default is 160) sampling points uniformly distributed
    over b=(1,0) to b=(0,1). Find the optimal policies (maximum values) at these
    points and return the combination these policies.
    """
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

      # judge whether max_poi is not in optimal:
      if all(any(max_poi != _) for _ in optimal):
        optimal.append(max_poi)

  """
  return the list back to dictionary in case we may want check 
  which action the value is for.
  """
  optimal_dict = defaultdict(list)
  for value in optimal:
    for act in values_input:
      # judge whether 'value' is in 'values_input[act]':
      if any(all(value == _) for _ in values_input[act]):
        optimal_dict[act].append(value)

  return optimal_dict