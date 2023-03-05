# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    root - parents.index(-1)
    height = 1 
    while parents[root] != -1:
        root = parents[root]
        height = height +1
    return height

def main():
    while True:
        newInput = input("ievadiet 'I', lai ievadītu no tastatūras vai 'F', lai ievadītu no faila:")
        if newInput == "I":
            n = int(input("Ievadiet 'node' skaitu:"))
            parents = list(map(int,input("ievadiet koka vecāku skaitu:")))
            break
        elif newInput == "F":
            fileName = input("Ievadiet faila nosaukumu:")
            if "a" in fileName:
                print("faila nosaukumā nevar būt burts 'a'")
                return 1
            try:
                n = int(fileName.readline())
                parents = list(map(int, fileName.readline().split()))
                break
            except FileNotFoundError:
                print("fails netika atrasts, pārbaudiet faila pareizrakstību")
                return 1 
        else:
            print("nepareiza izvēla, ievadiet tikai 'I' vai 'F'")
    height = compute_height(n , parents)
    print(height)            


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
