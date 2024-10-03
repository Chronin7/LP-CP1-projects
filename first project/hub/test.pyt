import time
import random
while True:
    inp = input("what:")
    for x in inp:
        print(x,end="")
        time.sleep(random.uniform(0,.3))
    print(end="\r\n")
