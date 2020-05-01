# 输入第一行包含一个正整数n，表示有n名选手。(1<=n<=100000)
#
# 输入第二行包含n个正整数，表示序列A。(0<=A[i]<=10^9)
#
# 输出
# 输出包含n行，每行一个正整数，第i行的正整数表示i号选手的排名是多少。即输出是一个1~n的排列。
#
#
# 样例输入
# 4
# 1 2 1 2
# 样例输出
# 1
# 4
# 2
# 3

#用栈解决

a = [x for x in range(1,5)]
aa = {x for x in range(1,5)}
b = [1,2,1,2]

stack ={}
for i in range(len(b)):
    a1 = b[0]
    # 入栈

    stack.pop(a[b[i]])
    x = set(aa) - set(stack)
    print(set(aa) - set(stack))