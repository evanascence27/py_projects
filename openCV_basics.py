#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import matplotlib.pyplot as plt
cv2.__version__


# In[19]:


color_img = cv2.imread("j_vermeer.jpg", 1);
gray_img = cv2.imread("j_vermeer.jpg", 0);
#print("Color Image array:\n", color_img)
#print("Gray Image array:\n", gray_img)
#cv2.startWindowThread()
#cv2.namedWindow("preview")


# In[20]:


#displaying image using opencv
# Show the image
cv2.imshow("J Vermeer colored", color_img)

# Prompt the user to press 's' to save the image
print("press 's' to save the image as vermeer_colored.jpg\n")

# Bind the waitKey function
# NOTE: if you are using a 32-bit machine, this needs to be: key = cv2.waitKey(0)
key = cv2.waitKey(0) & 0xFF

# wait for the ESC key to exit
if key == 27:
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif key == ord('s'): 
    cv2.imwrite("F:/AIProject/myProjects/images/vermeer_colored.jpg", color_img)
    cv2.destroyAllWindows()

cv2.imshow("J Vermeer grayscale", gray_img)
print("press 's' to save the image as vermeer_colored.jpg\n")
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'): 
    cv2.imwrite("F:/AIProject/myProjects/images/vermeer_colored.jpg", color_img)
    cv2.destroyAllWindows()


# In[21]:


#displaying image read using opencv using matplotlib
plt.title('How OpenCV images (BGR) display in Matplotlib (RGB)')
plt.imshow(gray_img)
plt.show()
rgb_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
plt.title('Correct Display after converting with cv2.COLOR_BGR2RGB')

# Tip: passing in empty lists for xticks & yticks will 
# turn them off 
plt.imshow(rgb_img)
plt.xticks([])
plt.yticks([])
plt.show()

