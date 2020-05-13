from skimage import io
from skimage import feature as ft
from skimage import util

img=io.imread('../pics/train1.jpg', True)
edge1=ft.canny(img)
e1=util.img_as_uint(edge1) 
io.imsave('../pics/edgeCanny1.png',e1)

edge3=ft.canny(img, sigma=3)
e3=util.img_as_uint(edge3)
io.imsave('../pics/edgeCanny3.png',e3)

edge5=ft.canny(img, sigma=5)
e5=util.img_as_uint(edge5)
io.imsave('../pics/edgeCanny5.png',e5)

