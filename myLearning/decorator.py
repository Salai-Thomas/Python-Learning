#Decorator From Deep Dive python

"""
Decorator ဆိုတာ မူရင်းရှိပြီးသား function or object တစ်ခုထဲကို လုပ်ဆောင်ချက် အသစ်တွေ ထပ်ထည့်လိုတဲ့အခါမှာ အသုံးပြုပါတယ်။ 
ထိုလုပ်ဆောင်ချက်တွေ ထပ်ထည့်တဲ့အခါ မူရင်းရှိပြီးသား function or object တွေထဲမှာ ရှိတဲ့ code structure ကို modify ပြုလုပ်ခြင်းမရှိပါ။
Decorator တွေဟာ map function တွေလို function တစ်ခု ကို argument တစ်ခုအနေနဲ့ ယူပါတယ်။ return အနေဖြင့် clourser တစ်ခုကို ပြန်ပေးတယ်။
"""

def myFun(x,y): # မူရင်းမပြောင်းလဲလိုသော function
    print(x/y)

def working(func): # decorator
    def inner(x,y): 
        if x< y: 
            x,y = y, x 
            return func(x,y) 
    return inner 

result=working(myFun)
result(5,10) 

# outer function para မှာ func တစ်ခု လက်ခံ inner fun မှာ parameter function ကို return
# ပြီး ရင် inner functio ကို return

# ပြန်ခေါ်တဲ့ခါ မူရင်းမပြောင်းလဲလိုတဲ့ function ကိုခေါ် para မှာ decorator ကိုရေး

"""
In Python, a decorator is a design pattern and a special type of function
that is used to modify the behavior of another function or method. 
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# When you call say_hello, it is actually calling the wrapper function created by my_decorator.
say_hello()

#@property

"""
@property ကို decorator တွေနဲ့တွဲသုံး ထိုသို့သုံးခြင်းဖြင့် ဖတ်ရလွယ်ကူစေ
"""

def dec_1(fn):
    def inner():
        print('running decorator 1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('running decorator 2')
        return fn()
    return inner

@dec_1 
@dec_2 
def myFun():
    print('Running myFun')

myFun()
#myNewFun = dec_1(dec_2(myFun))

# Output:
# running decorator 1
# running decorator 2
# Running myFun

@dec_1
def use_dec1_fun():
    print('using dec1')

use_dec1_fun()


# ပုံမှန် decorator function ကိုခေါ်တဲ့ အခါ မပြောင်းလဲလိုတဲ့ function ကို para အဖြစ်ပေးမယ့်အစား
# decorator ကို @ နဲ့တွဲခေါ်ပြီးမှ သူ့အောက်မှာ မူရင်းမပြောင်းလဲလိုတဲ့ function ကို သုံး
