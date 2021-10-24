#edge detection using robert cross operator
import cv2
import numpy as np
img = cv2.imread('Edge.tif',0)
m,n = img.shape
img_x = np.zeros((m,n), dtype = int)
img_y= np.zeros((m,n), dtype = int)
img_r = np.zeros((m,n), dtype = int)
for i in range(0,m):
    for j in range(0,n):
        if i==m-1 or j==n-1:
            img_x[i,j]=0
            img_y[i,j]=0
        else:
            lx=[]
            ly=[]
            lx=[img[i,j],img[i,j+1]*0,img[i+1,j]*0,img[i+1,j+1]*-1]
            ly=[img[i,j]*0,img[i,j+1],img[i+1,j]*-1,img[i+1,j+1]*0]
            s1=sum(lx)
            s2=sum(ly)
            img_x[i,j]=s1
            img_y[i,j]=s2
for i in range(0,m):
    for j in range(0,n):
        img_r[i,j]=(img_x[i,j]*2+img_y[i,j]*2)*(1/2)
cv2.imwrite('robert_edge.jpg', img_r)
