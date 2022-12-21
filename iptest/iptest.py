import os

with open('ip.txt', 'r') as f:
    a = f.readlines()[0]
    print(a)
    b = a.split(',')
    with open('wait.txt', 'w') as f1:
        for i in range(0, len(b)):
            f1.write(b[i] + '\n')
    f1.close()
f.close()

os.system("CloudflareST.exe -f wait.txt")

with open('result.csv', 'r', encoding='UTF-8') as f:
    c = f.readlines()
    with open('jieguo.txt', 'w') as f1:
        for i in range(1, len(c)):
            if i == len(c):
                f1.write(c[i].split(',')[0])
                break
            f1.write(c[i].split(',')[0] + ',')
    f1.close()
f.close()
