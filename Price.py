money=float(input('Enter the price:'))
if money < 75:
    print('The price:',money);
elif money > 75:
    print('The price:',money-15);
elif money > 100:
    print('The price:', money-25);
elif money > 150:
    print('The price:', money-50);
