# to delete .git
import os
import shutil

lis = []
for i in os.listdir(os.getcwd()):
    path = os.getcwd() + '/' + i
    if os.path.isdir(path):
        lis.append(path)
while len(lis) != 0:
    path = lis[0]
    lis = lis[1:]
    for k in os.listdir(path):
        k = path + '/' + k
        print(k, k[-4:-1] + k[len(k) - 1])
        if k[-4:-1] + k[len(k) - 1] == '.git':
            if os.path.isdir(k):
                shutil.rmtree(k)
            else:
                os.remove(k)
        elif os.path.isdir(k):
            lis.append(k)
