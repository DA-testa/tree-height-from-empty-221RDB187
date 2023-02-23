import sys
import threading


def compute_height(n, parents):
    max_height = 0
    heightList = [0] * n
    for x in range(n):
        height = 1
        i = parents[x]
        if i != -1 and heightList[i]!=0:
            heightList[x] = heightList[i]+1
            if max_height < heightList[x]: max_height = heightList[x]
            continue
        while i != -1:
            i = parents[i]
            height += 1
            if i != -1 and heightList[i]!=0:
                height = height + heightList[i]
                break
        if max_height < height: max_height = height
        heightList[x] = height
        i = parents[x]
        while i != -1:
            if i != -1 and heightList[i]!=0:
                break
            height -= 1
            heightList[i] = height
            i = parents[i]
    return max_height

def main():
    input_type = input("Enter 'F' to input from file or 'I' to input from keyboard: ")
    if input_type == 'F':
        file_name = input("Enter the file name: ")
        with open(file_name, mode="r") as f:
            n = int(f.readline().strip())
            arr = list(map(int, f.readline().strip().split()))
            print(compute_height(n, arr))
    else:
        n = int(input("Enter the number of nodes: ").strip())
        arr = list(map(int, input("Enter the parent of each node separated by space: ").strip().split()))
        print(compute_height(n, arr))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()