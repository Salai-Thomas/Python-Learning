name = "Techonology"
print(name)
#start inclusive /end exclusive /step
print(name[0:4])    #Tech
print(name[0:5:2])  #Tco
print(name[0:5:1])  #Techo  step 1 is default
print(name[::])     #Techonology
print(name[:])     #Techonology
print(name[-1])     #y      နောက်ဆုံးကကောင်ကိုထုတ်ပေး
print(name[1:])     #echonology index 1 ကစပြီးတောက်ရှောက်ထုတ်
print(name[0:-1])   #Techonolog  last index ကိုချန်
print(name[::-1])   #ygolonohceT Reverse ထုတ်
print(name[-1:-7:-1])#string Reverse ကို slicing ထပ်လုပ်ချင်ရင် step အဆင့်ပါထည့်ရေးပေးရ
print(ord('a'))
print(name * 3)
print(chr(98))
print('g' in name)