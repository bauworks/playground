data = [1,2,3]
for i in range(len(data)):
    data[i] = str(data[i])

csvdata = ",".join(data)
print(csvdata)