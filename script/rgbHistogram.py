from matplotlib import pyplot as plt
from skimage import io

img=io.imread('../pics/baboon.png')
red=img[:,:,0]
row,column=red.shape
r=red.reshape(row*column)
green=img[:,:,1]
row,column=green.shape
g=green.reshape(row*column)
blue=img[:,:,2]
row,column=blue.shape
b=blue.reshape(row*column)
f,(ax1, ax2, ax3)=plt.subplots(1,3)
n1, bins1, patches1 = ax1.hist(r, 256, facecolor='red')
ax1.set_title('Red component histogram')
n2, bins2, patches2 = ax2.hist(g, 256, facecolor='green')
ax2.set_title('Green component histogram')
n3, bins3, patches3 = ax3.hist(b, 256, facecolor='blue')
ax3.set_title('Blue component histogram')
plt.show()
