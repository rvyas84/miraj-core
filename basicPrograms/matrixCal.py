from numpy import array
from numpy import matrix

m1 = array([
    [1,2,3],
    [4,5,6]
])
print(m1)
print()

m2 = matrix('1 2 3;4 5 6;7 8 9')
m3 = matrix('1 2 3;4 5 6;7 8 9')

print(m2)

m4 = m3 + m2
print(m4)