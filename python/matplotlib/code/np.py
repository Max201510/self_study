import numpy as np

x = [[ 1., 0., 0.], [ 0., 1., 2.]]
x = np.array(x)
print(x.ndim)
print(x.shape)
print(x.size)
print(x.dtype)
print(type(x))

a = np.array([2,3,4])
print(type(a))

b = np.array([1,2,3])
c = [1,3,4]
m = b[b<3]

height = [2.7, 2.3,1.0,1.9]
np_height = np.array(height)
print(np_height)
print(np.array([True, 1, 2]) + np.array([3, 4, False]))
print(np_height[2:3])