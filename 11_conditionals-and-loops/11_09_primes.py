# Print out every prime number between 1 and 1000.
for i in range(1, 1000):
    if i != 1:
        #print("i = ", i)
        for s in range(2,i):
            if i % s == 0:
                break
        else:
            print("found a prime", i)