import numpy as np
calculations = {}
def calculate(list):
    array_1 = np.array(list)
    if len(list)<9:
      raise ValueError("List must contain nine numbers.")
    else:
      new_array = array_1.reshape(3,3)
    calculations['mean'] = [(new_array.mean(axis=0).tolist()), (new_array.mean(axis=1).tolist()),(new_array.mean().tolist())]
  
    calculations['variance'] = [(new_array.var(axis = 0).tolist()), (new_array.var(axis = 1).tolist()), (new_array.var().tolist())]
  
    calculations['standard deviation'] = [(new_array.std(axis = 0).tolist()), (new_array.std(axis = 1).tolist()),(new_array.std().tolist())]
  
    calculations['max'] = [(new_array.max(axis = 0).tolist()), (new_array.max(axis = 1).tolist()), (new_array.max().tolist())]

    calculations['min'] = [(new_array.min(axis = 0).tolist()), (new_array.min(axis = 1).tolist()),(new_array.min().tolist())]

    calculations['sum'] = [(new_array.sum(axis = 0).tolist()), (new_array.sum(axis = 1).tolist()), (new_array.sum().tolist())]
  

    return calculations