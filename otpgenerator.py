import random as r
i=10


def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgen()
while (i>=0):
    print(r.randint(0,9000)+1000)
    i=i-1
