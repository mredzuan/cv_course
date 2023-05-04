import numpy as np
import matplotlib.pyplot as plt

from PIL import Image #Load python image library

img = Image.open("course_file/CV_Python/DATA/00-puppy.jpg")
type(img)

#convert image to np array

img_arr = np.asarray(img)
img_arr.shape

plt.imshow(img_arr)
plt.show()


# Red channel - 0 (pure black) - 255 (full red)
img_red = img_arr.copy()
img_red.shape

plt.imshow(img_red[:,:,0], cmap="gray")
plt.show()


# Green channel
plt.imshow(img_red[:,:,1], cmap="gray")
plt.show()


# Blue channel 
plt.imshow(img_red[:,:,2], cmap="gray")
plt.show()


#remove G & B channel
img_red[:,:,1] = 0
img_red[:,:,2] = 0

plt.imshow(img_red)
plt.show()

img_red.shape


