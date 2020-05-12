from skimage import io
from skimage import exposure as ex
from matplotlib import pyplot as plt

img=io.imread('../pics/baboon.png', True)
imgEq=ex.equalize_adapthist(img)
io.imsave('../pics/baboonAdapthist.png', imgEq)
y,x=ex.histogram(imgEq)
c=plt.plot(x,y,color='gray')
plt.show()
