while True:
 w = float(input(" Nhập chiều rộng w= "))
 if (w<=0.0) and (w<=100.0) :
     break
 else:   
  print(" sai, nhập lại: ")
while True:
 h = float(input(" Nhập chiều dài h= "))
 if 0.0<=h<=100.0:
   break
 else:
     print(" sai, nhập lại:")
 
chu_vi = ( w + h )*2
dien_tich = w*h
print(f" chu vi hình chữ nhật:{chu_vi:.2f}")
print(f" diện tích hình chữ nhật:{dien_tich:.2f}")
