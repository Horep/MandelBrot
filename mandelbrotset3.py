import numpy as np
import matplotlib.pyplot as plt
import time

# Position of box to render
T=1 # top y coordinate
B=-1 # bottom y coordinate
R=1 # right x coordinate
L=-2 # left x coordinate
iterations=100 # how many iterations of the algorithm should be applied to each point
res=0.001 # determines the resolution of the graph

start=time.time() # used to measure the amount of time taken
x = np.arange(L, R, res) # divides up the box
y=  np.arange(B, T, res)
xx, yy = np.meshgrid(x, y, sparse=True) # sparse, assuming most of the boxes will instantly explode
print("Calculating",x.size*y.size,"squares","up to",iterations,"times.")
xx_0=xx
yy_0=yy
iter_array=np.zeros((y.size,x.size))
for i in range(iterations): # perform mandelbrot algorithm `iterations` times
    xtemp=(xx*xx-yy*yy +xx_0)
    yy=2*xx*yy +yy_0
    xx=xtemp
    iter_array = iter_array+((xx*xx+yy*yy) <2)

p=iter_array*(iter_array<iterations) # used to remove areas which should look black
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
