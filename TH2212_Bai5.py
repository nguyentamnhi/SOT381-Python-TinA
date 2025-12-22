def tinhS(n):
    TS = 0
    for i in range(1,n+1):
        TS = TS + i
        print(" TS=",TS)
    MS = 0
    for i in range(1,n//2+1):
        MS = MS +2*i
        print(" MS=",MS)
    S = TS/MS
    return S
n= int(input("nhập n="))
print(" tính S:", tinhS(n))