from skimage import io
from skimage.filters.rank import mean
from skimage.morphology import square, disk

imgNoise=io.imread('../pics/baboonNoise.png')
a1=square(3)
a2=square(5)
imgDeNoise=mean(imgNoise,a1)
io.imsave('../pics/baboonSquare3.png', imgDeNoise)
imgDeNoise=mean(imgNoise,a2)
io.imsave('../pics/baboonSquare5.png', imgDeNoise)
a1=disk(1)
a2=disk(2)
imgDeNoise=mean(imgNoise,a1)
io.imsave('../pics/baboonDisk1.png', imgDeNoise)
imgDeNoise=mean(imgNoise,a2)
io.imsave('../pics/baboonDisk2.png', imgDeNoise)
