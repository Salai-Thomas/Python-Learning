#conditional statement

price = 200

if price >=300:
    actual_price = price -(price * 0.3)
    print(f"You get 30% Discount.So your charge is {actual_price}")
elif price >=200:
    price *= 0.8
    print(f"You get 30% Discount.So your charge is {price}")
elif price >=100:
    price *= 0.9
    print(f"You get 30% Discount.So your charge is {price}")
else:
    print('no discount')


