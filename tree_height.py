# python3

import sys
import threading


def compute_height(n, parents):
    heights = [0] * n
    max_height =0

    for i in range(n):
        parent = parents[i]
        height = 1
         
        while parent != -1:
              if heights[parent] != 0:
                   height = height + heights[parent]
                   break
              height = height +1

              parent = parents[parent]

        heights[i] = height
        max_height = max(max_height, height)

    return max_height
          
    
    


def main():
        
        newInput = input()

        if newInput == "I":
            n = int(input())
            parents = list(map(int,input().split()))
            print(compute_height(n, parents))

        elif newInput == "F":
            fileName = input()
            if "a" in fileName:
                with open("./test/" + fileName, "r") as files:
                    n2 = int(files.readline())
                    parents2 = list(map(int, files.readline().split()))
                    print(compute_height(n2, parents2))



    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
