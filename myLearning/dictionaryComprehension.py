# marks = {"kyaw kyaw":100,'Aung aung':100,"Mya Mya":200,"Su Su":220}

# moration ={name:mark +20 for (name,mark) in marks.items() if mark == 100}
# print(moration)

import random
students = ["Aung Aung","Kyaw Kyaw","Su Su","Hla Hla"]
marks = {name:random.randint(1,100) for name in students}
print(marks)