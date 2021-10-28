import random as r

i=10

def otpgeneration():
    otp=" "
    for i in range(5):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is generated: ")
    print (otp)
otpgeneration()
while (i>=0):
    print(r.randint(0,9000)+1000)
    i=i-1
