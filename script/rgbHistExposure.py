from matplotlib import pyplot as plt
from skimage import io
from skimage import exposure as ex

img=io.imread('../pics/baboon.png')
red=img[:,:,0]
green=img[:,:,1]
blue=img[:,:,2]
f,(ax1, ax2, ax3)=plt.subplots(1,3)
hist1,bin_centers1=ex.histogram(red)
ax1.plot(bin_centers1,hist1,color='red')
ax1.set_title('Red component histogram')
hist2,bin_centers2=ex.histogram(green)
ax2.plot(bin_centers2,hist2,color='green')
ax2.set_title('Green component histogram')
hist3,bin_centers3=ex.histogram(blue)
ax3.plot(bin_centers3,hist3,color='blue')
ax3.set_title('Blue component histogram')
plt.show()
