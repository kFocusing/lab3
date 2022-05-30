import matplotlib.pyplot as plt
import numpy as np
import math
import statistics

n = 50
np.random.seed()
x = 2+np.random.normal(2, 1.5, n)
print(x)
k = int(1.448*math.log(n)+1)
 
fig, ax = plt.subplots()

ax.hist(x, bins=k, linewidth=0.5, edgecolor="white", orientation='horizontal')

plt.show()
y=list(range(0,n))

print("min: ",min(x))
print("max: ",max(x))
avrg=statistics.mean(x)
print("MIddle: ",avrg)
print("S: ",np.std(x))


plt.scatter(y,x)
plt.show()
c=False
while(c!=True):
    c=True
    Tmax=(max(x)-statistics.mean(x))/np.std(x)
    index_max=np.argmax(x)
    Tmin=(statistics.mean(x)-min(x))/np.std(x)
    index_min=np.argmin(x)
    print("min: ",min(x))
    print("max: ",max(x))
    if(Tmax>1.962):
        c=False
        x[index_max]=avrg
    if(Tmin>1.962):
        c=False
        x[index_min]=avrg
plt.scatter(y,x)
plt.show()

