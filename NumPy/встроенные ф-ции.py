import numpy as np

# =============================================================================
# c = np.eye(4,2)
# print(c)
# print('\n')
# c = np.eye(3,2, dtype=int)
# print(c)
# print('\n')
# c = np.zeros((3,3), dtype=int)
# print(c)
# print('\n')
# c = np.ones((4,6), dtype=int)
# print(c)
# =============================================================================

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
b = a[0:2, 0:2, 0:2]
print(b)