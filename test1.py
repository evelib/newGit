str2 ="3nf0a8833nss9"
y = list(str2)
print(y)
k = []

for i in range(len(y)):
    if (y[i] <= "9" and y[i] >= "0"):
        y[i] = int(y[i])
        k.append(y[i])


print(k)