import numpy as np 

#a = np.random.randint(0,3, size=30)

r = np.random.rand(9,5)
a = np.round(4*r[:,0])

res = [a[i] == 0 and a[i] == a[i+1] for i in range(len(a)-1)]
res.insert(-1, False)

corrected = a[np.where(np.array(res)==False)]
corrected2 = r[np.where(np.array(res)==False)]

print(r)
print(a)
print(corrected)
print(corrected2)

#wrong -> second was removed

print('')
