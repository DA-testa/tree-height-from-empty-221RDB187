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
    input_type = input("F or I")
    if input_type == 'F':
        file_name = input("Enter the file name: ")
        if 'a' in file_name:
            return
        if "/test" not in file_name:
            file_name = "test/" + file_name
        with open(file_name) as f:
            lines = f.readlines()
            n = int(lines[0])
            arr = list(map(int, lines[1].split()))
            height = compute_height(n, arr)  
    elif  "I" in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)

    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
