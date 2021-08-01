from math import *
from random import random

otpData='0123456789'
leng=len(otpData)
otp=''
for i in range(4):
    otp+=otpData[math.floor(random.random()*leng)]

print(otp)