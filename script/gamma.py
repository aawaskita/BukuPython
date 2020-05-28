from skimage import io
from skimage.exposure import adjust_gamma as ag

img=io.imread('../pics/baboon.png')
img1=ag(img,0.5)
io.imsave('../pics/baboonGammaHalf.png', img1)
img2=ag(img,2)
io.imsave('../pics/baboonGammaDouble.png', img2)
