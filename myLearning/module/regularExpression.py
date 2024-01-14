import re

my_str = "h12"

m = my_str
# print(re.match("[a-z][0-9]",m))

# print(re.search("[a-z][0-9]",my_str))
# print(re.search("[0-9][0-9][0-9]",my_str))  #0 to 9 ဂဏာန်းသုံးလုံးဆင့်ပါသလား
# print(re.search("[a-z][0-9]",my_str))
# print(re.search("[abc]","somethingcab"))      # a or b or c ရှေ့ဆုံးမှလာသောကောင်ကိုပဲဖမ်းပေး

# print(re.search("1.4","158"))              # . means any value
# print(re.search("^Java","Java"))         #start
# print(re.search("Java$","programming of java"))   # end

# print(re.search("[a-z]*[1-9]*",""))#ဘာမှမပါလဲ 0 နဲ့ match ဖြစ် a to z ကြိုက်သလောက်လာ  1 to 9 ကြိုက်သလောက်လာ၏
# print(re.search("[a-z]+[1-9]+","s1"))

# print(re.search("[a-z]+[1-9]?","s1")) # 0 or 1 ပိုရင်လဲ match ဖြစ်ဆက်မယူ
# print(re.search("[1-9]{2,6}","1237"))
# print(re.search("\w+","1237_se99*%9"))

# print(re.search("\s*","     hello "))
# print(re.search("\S*","hello "))
# print(re.search("\bhello","helloWorld"))
# m = re.search("([a-z]*)\.py","hello.py")
# print(m.groups())

# m = re.search("(http|https)://(www\.\w+\.(com|org|gov))","https://www.google.com")
# print(m)

# m = re.match("(http|https)://(www\.\w+\.(com|org|gov))","https://www.google.com something")
# print(m.match())

# m = re.fullmatch("(http|https)://(www\.\w+\.(com|org|gov))","https://www.google.com something")
# print(m)

# lst = re.findall("(http|https)://(www\.\w+\.(com|org|gov))","https://www.google.com something https://www.yahoo.com")
# print(lst)

# for i in lst:
#     print(i)

# iter = re.finditer("(http|https)://(www\.\w+\.(com|org|gov))","https://www.google.com something https://www.yahoo.com")
# print(iter)

# for i in iter:
#     print(i)

# replace = re.subn("(http|https)://(www\.\w+\.(com|org|gov))","domain","https://www.google.com something https://www.yahoo.com")
# print(replace)

# sp_string = re.split(",","www,google,com")
# print(sp_string)

# print(re.search("(http|something)","somehting"))


