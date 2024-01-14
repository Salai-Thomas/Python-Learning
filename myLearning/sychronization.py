import threading

counter = 0

def increment():
    global counter
    for i in range(0,200000):
        counter +=1

def decrement():
    global counter
    for i in range(0,200000):
        counter -=1

firsThread = threading.Thread(target=increment)
secThread = threading.Thread(target=decrement)

firsThread.start()
secThread.start()

firsThread.join()
secThread.join()
print(counter)       