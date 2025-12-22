def solonnhat_vasonhonhat(a,b,c):
    
    LN=a
    if b>LN:
        LN=b
    if c>LN:
        LN=c
    NN=a
    if b<NN:
       NN=b
    if c<NN:
       NN=c
    return LN,NN
a= int(input(" a="))
b= int(input("b="))
c= int(input("c="))
LN,NN= solonnhat_vasonhonhat(a,b,c)
print(" số lớn nhất :",LN)
print(" số nhỏ nhất :",NN)