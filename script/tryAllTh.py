from skimage import io
from skimage.filters import try_all_threshold as allth
from matplotlib import pyplot as plt

a=io.imread('../pics/tulips.png', as_gray=True)
fig, ax = allth(a, figsize=(10, 8), verbose=False)
plt.show()
