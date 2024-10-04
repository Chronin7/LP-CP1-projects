
if False:
    import pickle

    # Pickle a simple object
    my_object = {'name: Alice, age: 30'}
    with open('my_object.pickle', 'wb') as f:
        pickle.dump(my_object, f)

    # Unpickle the object
    with open('my_object.pickle', 'rb') as f:
        loaded_object = pickle.load(f)

    # Print the unpickled object
    print(loaded_object) # Output: {'name': 'Alice', 'age': 30}
import os
def send2():
    path = '/LP-CP1-PROJECTS/hub/pickles/'
    arr = os.listdir(path)
    for x in arr:
        xpath = os.path.join(path,x)
        with open(xpath, 'rb') as fh:
            while True:
                # send in 1024byte parts
                chunk = fh.read(1024)
                if not chunk: break
                ser.write(chunk)

import serial
import pickle
bob = "#"
with open ('bob.pickle', 'wb') as f:
    pickle.dump(bob, f)
while True:
    no_quote = 1
    in_alredy = 0
    imp = input("name a chericter:")
    if imp == "":
        print("sorry not in the databace yet")
        no_quote = 0
    if imp == "":
        print("sorry not in the databace yet")
        no_quote = 0
    if imp == "call data":
        with open('quotes.pickle', 'rb') as f:
            loaded_object = pickle.dump(f)
            print(loaded_object)
    if no_quote == 1:
        print("not in the database yet")
        quotes = {input("what is a quote (note i go thru this so it wont aoutomaticly add the quote):")}
        with open('quotes.pickle', 'rb') as f:
            pickle.dump(quotes, f)
