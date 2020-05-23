with open("jinko.txt") as f:
    while True:
        l = f.readline()
        print(l.strip())
        if not l:
            break
