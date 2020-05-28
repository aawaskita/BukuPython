from skimage import io
from skimage.exposure import adjust_log as al

img=io.imread('../pics/baboon.png')
img1=al(img)
io.imsave('../pics/baboonLog.png', img1)
img2=al(img, inv=True)
print(img1.mean(), img.mean(), img2.mean())
io.imsave('../pics/baboonInvLog.png', img2)
