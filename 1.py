#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = "images/filename.png"

im = cv2.imread(filename,0)

# removing small noise from the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
eroded_im = cv2.erode(im, kernel, iterations=1)
dilated_im = cv2.erode(eroded_im, kernel, iterations=1)

# plt.imshow(dilated_im,cmap='gray')

_, labels, stats, _ = cv2.connectedComponentsWithStats(dilated_im)

# plt.imshow(labels,cmap='gray')

colors = np.unique(labels)
colors

rect_col = (0, 0, 255)
thickness = 2
offset = 3

boxes = []
for c in colors:
    if c==0:
        continue
    temp = np.argwhere(labels==c)
    min_x = min(temp[:,1])
    min_y = min(temp[:,0])
    max_x = max(temp[:,1])
    max_y = max(temp[:,0])
    
    if min_x>=offset:
        min_x -= offset
    if min_y>=offset:
        min_y -= offset
    if max_x<(im.shape[0]-offset):
        max_x += offset
    if max_y<(im.shape[1]-offset):
        max_y += offset
        
    vis = cv2.rectangle(np.zeros((im.shape[0],im.shape[1],3)).astype('uint8'), (min_x, min_y), (max_x, max_y), rect_col, thickness)
    plt.imshow(vis)
    plt.show()
    
    w = abs(max_x - min_x)
    h = abs(max_y - min_y)
    centre = (min_x+(w//2), min_y+(h//2))
    
    box = [centre[0],centre[1],w,h]
    boxes.append(box)
    
print(boxes)


# In[ ]:





# In[ ]:




