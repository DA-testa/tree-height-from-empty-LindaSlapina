# python3

import sys
import threading


def compute_height(n, parents):
    tik={}
    def height(i):
        if i in tik:
            return tik[i]
        if i==-1:
            return 0
        c=1+height(parents[i])
        tik[i]=c
        return c
    max_height=0
    for i in range(n):
        max_height=max(max_height, height(i))
    return max_height

def main():
        newinput = input()
        if "I" in newinput:
            a = int(input())
            b = list(map(int,input().split()))
            print(compute_height(a,b))
        if "F" in newinput:
            filename = input()
            if "a" not in filename:
                with open("./test/"+filename, "r") as files:
                    c = int(files.readline())
                    d = list(map(int, files.readline().split()))
                    print(compute_height(c,d))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
