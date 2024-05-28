def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1
for n in nextSquare():
    if  n>25:
        break
    print(n)