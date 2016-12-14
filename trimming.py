import cv2
import os
import glob

width = 256
height = 384

for i in range(0,100):

    print i
    img = cv2.imread("./formal/"+str(i)+".jpg",cv2.IMREAD_UNCHANGED)

    hi,wi=img.shape[:2]
    xp = height * 1.0/hi
    yp = width*1.0/wi
    power = 0
    if xp > yp:
        power = xp
    else:
        power = yp

    sub = cv2.resize(img,(int(wi * power),int(hi * power)))
    hi,wi=sub.shape[:2]
    dst = sub[(hi-height)/2:(hi+height)/2,(wi-width)/2:(wi+width)/2]
    cv2.imwrite("./result/"+str(i)+".jpeg",dst)
    print "hi ",dst.shape[0]," wi",dst.shape[1]
