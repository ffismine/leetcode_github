# -*- coding:utf-8 -*-
# Author : Zhang Xie
# Date : 2020/5/24 21:30

PATH1 = './file1.txt'
PATH2 = './file2.txt'

with open(PATH1) as f1:
    f1_ = f1.read()
with open(PATH2) as f2:
    f2_ = f2.read()


l = list(f1_ + f2_)
l.sort()
all_str = "".join(l)
PATH3 = './file3.txt'
with open(PATH3, 'w') as f3:
    f3.write(all_str)






