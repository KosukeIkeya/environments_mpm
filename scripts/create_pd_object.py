from envtest import pd_create_object
import numpy as np

A = [1, 3, 5, np.nan, 6, 8]

print(pd_create_object(A))