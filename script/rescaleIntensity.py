from skimage import io
from skimage import exposure as ex
from matplotlib import pyplot as plt

img=io.imread('../pics/baboon.png',True)
f,(ax1, ax2, ax3)=plt.subplots(1,3)
bb1=ex.rescale_intensity(img, in_range=(0,1), out_range=(0,0.25))
io.imsave('../pics/baboonScale1.png', bb1)
hist1,bin_centers1=ex.histogram(bb1)
ax1.plot(bin_centers1,hist1,color='gray')
ax1.set_title('0 to 0.25')
bb2=ex.rescale_intensity(img, in_range=(0,1), out_range=(0.35, 0.6))
io.imsave('../pics/baboonScale2.png', bb2)
hist2,bin_centers2=ex.histogram(bb2)
ax2.plot(bin_centers2,hist2,color='gray')
ax2.set_title('0.35 to 0.6')
bb3=ex.rescale_intensity(img, in_range=(0,1), out_range=(0.75, 1))
io.imsave('../pics/baboonScale3.png', bb3)
hist3,bin_centers3=ex.histogram(bb3)
ax3.plot(bin_centers3,hist3,color='gray')
ax3.set_title('0.75 to 1')
plt.show()
