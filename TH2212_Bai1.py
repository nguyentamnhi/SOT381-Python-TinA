while True:
 w = float(input(" Nhập chiều rộng w= "))
 if 0.0<=w<=100.0 :
     break

while True:
 h = float(input(" Nhập chiều dài h= "))
 if 0.0<=h<=100.0:
   break
chu_vi = ( w + h )*2
dien_tich = w*h
print(f" chu vi hình chữ nhật:{chu_vi:.2f}")
print(f" diện tích hình chữ nhật:{dien_tich:.2f}")
