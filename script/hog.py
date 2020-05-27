from skimage import io
from skimage import feature as ft

img=io.imread('../pics/baboon.png')

hog1=ft.hog(img, orientations=1, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm='L2-Hys', visualize=True, transform_sqrt=False, feature_vector=True, multichannel=None)
hog2=ft.hog(img, orientations=10, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm='L2-Hys', visualize=True, transform_sqrt=False, feature_vector=True, multichannel=None)
print(hog1[0])
print(hog2[0])
io.imsave('../pics/bhog1.png', hog1[1])
io.imsave('../pics/bhog10.png', hog2[1])
