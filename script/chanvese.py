from skimage import io
from skimage import segmentation as sg
from matplotlib import pyplot as plt
from skimage import util

img=io.imread('../pics/train1.jpg',True)
cv1=sg.chan_vese(img, mu=0.25, lambda1=1, lambda2=1, tol=1e-3, max_iter=300, dt=0.5, init_level_set="checkerboard", extended_output=True)
e1=util.img_as_uint(cv1[0])
io.imsave('../pics/chanvesemu25.png',e1)
cv2=sg.chan_vese(img, mu=0.5, lambda1=1, lambda2=1, tol=1e-3, max_iter=300, dt=0.5, init_level_set="checkerboard", extended_output=True)
e2=util.img_as_uint(cv2[0])
io.imsave('../pics/chanvesemu5.png',e2)
cv3=sg.chan_vese(img, mu=0.75, lambda1=1, lambda2=1, tol=1e-3, max_iter=300, dt=0.5, init_level_set="checkerboard", extended_output=True)
e3=util.img_as_uint(cv3[0])
io.imsave('../pics/chanvesemu75.png',e3)

