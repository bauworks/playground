data = ["abc", "defgh"]
with open("writeexample2.txt", "w") as f:
    f.writelines(data[0])