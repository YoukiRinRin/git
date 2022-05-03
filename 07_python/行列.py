import numpy 

A = numpy.array([[3,1,2],[5,2,7]])
B = numpy.array([[5,1,7],[6,2,3]])
print(A + B)
print(A-B)

C = numpy.array([[1,2],[3,4]])
print(3 * C)

a = numpy.array([1,2,3])
b = numpy.array([10.100,1000])

print(numpy.inner(a,b))

print('shape:',b.shape)
