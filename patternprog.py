num = int(input("Enter No.of.Rows:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
#Print heart shape 
for row in range (6):
    for col in range (7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("v",end="")
        else:
            print(" ",end="")
    print()
    
#Chess board using numpy
import cv2
import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((100,100), dtype=np.uint8)
white = np.ones((10,10),dtype=np.uint8)

black[0:10,0:10] = white #corner
black[10:20,10:20] = white

square = black[0:20,0:20]

chess = np.tile(square,(4,4))
plt.xticks([])
plt.yticks([])
plt.imshow(chess, cmap='gray')
 
    