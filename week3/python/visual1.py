import matplotlib.pyplot as plt
from PIL import Image
pil_im = Image.open('picture.jpg')
pil_im.thumbnail((128,128))
plt.imshow(pil_im)
plt.axis('off')
plt.show()