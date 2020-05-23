with open("jinko.txt") as f:
    l = f.readline()
    while l:
        l = f.readline()
        print(l.strip().split())
