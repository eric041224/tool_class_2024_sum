from PIL import Image
from pylab import *
im = array(Image.open('picture.jpg'))
imshow(im)
print ('Please click 3 points')
x = ginput(3)
print ('you clicked:',x)
show()