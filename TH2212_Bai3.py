def solonnhat(a,b,c):
    
    LN=a
    if b>LN:
        LN=b
    if c>LN:
        LN=c
    return LN
a= int(input(" a="))
b= int(input("b="))
c= int(input("c="))
print(" số lớn nhất :",solonnhat(a,b,c))