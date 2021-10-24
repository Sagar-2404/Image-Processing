import cv2
import numpy as np
img = cv2.imread('Edge.tif',0)
m,n = img.shape
img_x = np.zeros((m,n), dtype = int)
img_y= np.zeros((m,n), dtype = int)
img_r = np.zeros((m,n), dtype = int)
for i in range(0,m):
    for j in range(0,n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            img_y[i,j]=0
            img_y[i,j]=0
        else:
            l1=[]
            l2=[]
            l1=[img[i-1,j-1]*-1,img[i-1,j]*0,img[i,j-1]*-2,img[i,j]*0,img[i+1,j+1],img[i+1,j]*0,img[i,j+1]*2,img[i+1,j-1]*-1,img[i-1,j+1]]
            l2=[img[i-1,j-1],img[i-1,j]*2,img[i,j-1]*0,img[i,j]*0,img[i+1,j+1]*-1,img[i+1,j]*-2,img[i,j+1]*0,img[i+1,j-1]*-1,img[i-1,j+1]]
            s1=sum(l1)
            s2=sum(l2)
            img_x[i,j]=s1
            img_y[i,j]=s2
for i in range(0,m):
    for j in range(0,n):
        img_r[i,j]=(img_x[i,j]*2+img_y[i,j]*2)*(1/2)
cv2.imwrite('soble_edge.jpg', img_r)
