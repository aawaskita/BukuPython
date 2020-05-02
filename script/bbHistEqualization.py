from matplotlib import pyplot as plt
from skimage import io, exposure as ex

img=io.imread('../pics/baboonGS.png')
imgEq=ex.equalize_hist(img,nbins=256)
hist,bins=ex.histogram(imgEq)
c=plt.plot(bins,hist,color='gray')
io.imsave('../pics/baboonGSEq.png',imgEq)
plt.show()
