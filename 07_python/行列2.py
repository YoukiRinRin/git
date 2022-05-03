import numpy as np

a = np.array([1,2,3])
a2 = np.array([1,2,3,4])
a3 = np.array([1,2,3,4,5])
print(a.shape)
print(a2.shape)
print(a3.shape)

print(a.ndim)
print(a2.ndim)
print(a3.ndim)

b = np.array(
    [[1,2,3],
    [4,5,6],
    [7,8,9]]
)

print('Shape:',b.shape)
print('Rank:',b.ndim)

a = np.zeros((3,3))

print(a)

b = np.ones((2,3))

print(b)

c = np.full((3,2),9)
print(c)

d = np.eye(5)
print(d)

e = np.random.random((4,5))
print(e)

f = np.arange(3,10,1)
f2 = np.arange(3,10,2)
print(f)
print(f2)