#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.array([0, 1, 2])
print(type(a))


# In[3]:


import numpy as np
import cv2
get_ipython().run_line_magic('matplotlib', 'inline')
#Comment: The purpose of the above line is to display matplotlib plots inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[19]:


img_gogh = mpimg.imread("van_gogh.jpg")
resized1 = cv2.resize(img_gogh, (300, 350))
plt.imshow(resized1)
plt.title("The Starry Night")
plt.show()


# In[20]:


img_gogh = mpimg.imread("j_vermeer.jpg")
resized2 = cv2.resize(img_gogh, (300, 350))
plt.imshow(resized2)
plt.title("Girl with a Pearl Earring")
plt.show()


# In[43]:


blend = cv2.addWeighted(resized1,0.3,resized2,1,-5)
plt.imshow(blend)
plt.title("Blended Image")
plt.show()


# In[39]:


print("Thank you!")


# In[ ]:




