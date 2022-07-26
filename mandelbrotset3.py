import numpy as np
import matplotlib.pyplot as plt
import time


T=1
B=-1
R=1
L=-2
iterations=100
res=0.001

start=time.time()
x = np.arange(L, R, res)
y=  np.arange(B, T, res)
xx, yy = np.meshgrid(x, y, sparse=True)
print("Calculating",x.size*y.size,"squares","up to",iterations,"times.")
xx_0=xx
yy_0=yy
iter_array=np.zeros((y.size,x.size))
for i in range(iterations):
    xtemp=(xx*xx-yy*yy +xx_0)
    yy=2*xx*yy +yy_0
    xx=xtemp
    iter_array = iter_array+((xx*xx+yy*yy) <2)
    

    

    
    
p=iter_array*(iter_array<iterations)
end=time.time()

print("Set calculation completed in",round(end-start,2),"seconds")
print("Drawing Graph")
start=time.time()
h = plt.pcolormesh(x,y,p,cmap="magma")
plt.colorbar(label="iterations")
plt.xlim(L, R)
plt.ylim(B, T)
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('MandelBrot.png', dpi=3000,bbox_inches="tight")
plt.show()
end=time.time()
print("Graph calculation completed in",round(end-start,2),"seconds")