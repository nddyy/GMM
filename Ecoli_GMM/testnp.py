import numpy as np

signalH=np.array([[1.0,2.0,3.0,4.0,5.0],
                [6.0,7.0,8.0,9.0,10.0],
                [11.0,12.0,13.0,14.0,15.0],
                [16.0,17.0,18.0,19.0,20.0]],dtype=np.uint16)

signalL=np.array([[1.0,2.0,3.0,4.0,5.0],
                [6.0,7.0,8.0,9.0,10.0],
                [11.0,12.0,13.0,14.0,15.0],
                [16.0,17.0,18.0,19.0,20.0]],dtype=np.uint16)

acgtIndex=np.array([[0,1,2,3,4],
                [4,3,2,1,0],
                [0,1,2,3,4],
                [4,3,2,1,0]])


miu = np.mean(signalH[acgtIndex == 0])
print(miu)

# print(np.diag(sigma_square))

