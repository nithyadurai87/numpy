import numpy as np 

a1 = np.arange(24).reshape(4,3,2)
a2 = np.arange(12).reshape(3,4)

print (np.hstack((a1[-1],a1[-2])))
print (np.vstack((a1[-1],a1[-2])))

print (np.hsplit(a1,3))
print (np.vsplit(a1,2))
print (np.vsplit(a1,(3,3)))
print (np.hsplit(a1,(3,)))

a3 = np.array([[23,34,54,21],[75,88,70,79],[98,29,73,90]])
print (np.hstack((a2,a3))) 
print (np.vstack((a2,a3)))
