#Special Methods of python
#__str__
#__len__
#__dir__

class Book:
    def __init__(self,name,year,pages):
        self.name = name
        self.year = year
        self.pages = pages

    def __str__(self):
        return 'hello world'
    
    def __len__(self):
        return self.pages
    
    def __eq__(self,other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False

book1 = Book("Gone With The Wind",1999,500)
book2 = Book("Gone With The Wind",1999,50)

print(book1) #<__main__.Book object at 0x000001C5AC3DA7B0> {object 's memory address}
print(type(book1))  # <__main__.Book object at 0x000001C5AC3DA7B0>
print(len(book1)) # TypeError: object of type 'Book' has no len() // 500

print(book1 == book2) # False # True ပုံမှန် အားဖြင့် object ရဲ့ address နှစ်ခုစစ် but eq method ဖြင့် name and year တူရင် true ဖြစ်စေသောကြောင့် 
# behaviour ပြောင်းလဲ

# သူရဲ့ orginal behaviour တွေကို ပြောင်းလဲလိုက်ခြင်းကို overloading လုပ်တယ်လို့ခေါ်
