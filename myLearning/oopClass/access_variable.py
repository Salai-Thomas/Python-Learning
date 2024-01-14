class Parent:
    var_one = "var one of parent"
    def __init__(self):
        print("Parent constructor")
        self.var_two = "instance of parent"

    @staticmethod
    def static_method():
         print("static method")
    
    @classmethod
    def class_method(cls):
         print("class method")

class Child(Parent):
        def __init__(self):
            super().__init__()
            print("Child Constructor")
        def method(self):
             print("Super varone",super().var_one)
            #  print("instance vartwo",super().var_two)     #parent ရဲ့ instance ကိုယူသုံးခွင့်မရှိ
             super().static_method()
             super().class_method()

ch = Child()
ch.method()