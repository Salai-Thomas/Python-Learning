file = open("hello.txt","w")

file.write("hello")
file.write(" from python")

for i in range(1,101):
    file.write(str(i)+"\r\n")

    
file.seek(10,0)
file.write("hello")
file.close()

