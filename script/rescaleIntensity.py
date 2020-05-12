from skimage import io
from skimage import exposure as ex

img=io.imread('../pics/baboon.png',True)
print(img.min(), img.max())
bb1=ex.rescale_intensity(img, in_range=(0,1), out_range=(0,0.25))
io.imsave('../pics/baboonScale1.png', bb1)
bb2=ex.rescale_intensity(img, in_range=(0,1), out_range=(0.35, 0.6))
io.imsave('../pics/baboonScale2.png', bb2)
bb3=ex.rescale_intensity(img, in_range=(0,1), out_range=(0.75, 1))
io.imsave('../pics/baboonScale3.png', bb3)
