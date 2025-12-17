d=r=0
def nhap():
  global d,r  
  d=int(input("chiều dài= "))
  r=int(input("chiều rộng= "))
def tinhcv():  
  C=(d+r)*2
  return C
def tinhdt():
  S=d*r
  return S
def inra():
  print("chu vi hình chữ nhật là:",C)
  print("diện tích hình chữ nhật là:",S)   
nhap()
C=tinhcv()
S=tinhdt()  
inra()
