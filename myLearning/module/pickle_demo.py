import pickle

class Human:
    def __init__(self,name,age):
        self.name= name
        self.age = age

# h = Human("Python",40)
# with open("human.data","wb")as file:
#     pickle.dump(h,file)

with open("human.data","rb") as file:
    h = pickle.load(file)
    print(h.name,h.age)