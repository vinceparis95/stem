import numpy as np


#############################

# U n i t a r i t y

############################

# create the matrix

x = np.array([[0, 1],
              [1, 0]])

############################


def isUnitary(m):
    tmatrix = m.transpose()
    i = np.matmul(m, tmatrix)
    return i


print(isUnitary(x))


############################

# the E i g e n v a l u e

############################

# create the lamda (λ)

# set λ to 1
l = 1
# i matrix * λ
i = np.eye(2)
# dot λ with i
lam = (np.dot(i, l))
# subtract λi from  matrix
z = x - lam
print(z)

############################

# find the determinant

# det = det(A-λI)=0
def isEigen(input):
    det = input
    det2 = []
    for x in det:
        for y in x:
            det2.append(y)
    det3 = (det2[0] * det2[3]) \
         - (det2[1] * det2[2])
    if det3==0:
        print(det3)


isEigen(z)