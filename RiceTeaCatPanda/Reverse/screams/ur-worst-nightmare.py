import cv2 as               cv2
import soundfile as         soundfile
import random as            random
import numpy as             numpy
from tqdm import tqdm as    tqmd
import os as                os
import binascii as          binascii

g, h = cv2.imread("pls-no.jpg"), soundfile.SoundFile("oh-gawd-plsno.wav", 'r')
i, j = g.shape[0], 0
print("i : ",i)
k=numpy.zeros((i*i,2), dtype=numpy.float64)
print("numpy : ", k)
l, m = tqmd(total=i*i), h.read()
l.set_description(" nuKiNG")
print("tqmd : ",l)
print("sond : ",m)
h.close()
u=True

t = soundfile'9\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
v = soundfile'@\xe4\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(" t : ",t)
print(" v : ",v)

for n in range(0,i):
    for o in range(0,i):
        if u == True:

            p, q, r = g[n][o][0], g[n][o][1], g[n][o][2]; p, q, r = str(p), str(q), str(r)
                        #    me          me          me
            while len(p) < 3:
                p="0"+p
                while len(q) < 3:
                    q="0"+q
                    while len(r) < 3:
                        r="0"+r#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
            result = p+q+r
            for w in range(0, j+1):
                x=binascii.b2a_uu(t);                y=binascii.b2a_uu(v)
            t = binascii.a2b_uu("0.00")
            #         ww
            v = binascii.a2b_uu("-0.00")
            s=random.randint(0,1)
            if s == 0: k[j]=(m[j][0]*2,float(x.decode()[:-2].strip(" ")+result))
            if s == 1: k[j]=(m[j][0]*2,float(y.decode()[:-2].strip(" ")+result))
            j+=1
           #soundfile
            l.update(1)

            #wow   0   then
soundfile.write('out.wav', k, 44100, 'FLOAT')
