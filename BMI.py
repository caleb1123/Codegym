import math
BMI=float
weight=float(input('Enter the weight'))
height=float(input('Enter the height'))
height=height/100
BMI=weight/(height*height)
print(int(BMI))
if BMI < 16:
    print('Gầy cấp độ 3')
elif BMI <17:
    print('Gầy cấp độ 2')
elif BMI <18.5:
    print('Gầy cấp độ 1')
elif BMI <25:
    print('Bình Thường')
elif BMI < 30:
    print('Thừa cân')
elif BMI <35:
    print('Béo phì cấp 1')
elif BMI <40:
    print('Béo phì câp 2')
else :
    print('Béo phì cấp độ 3')