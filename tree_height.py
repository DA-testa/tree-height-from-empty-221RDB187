import sys
import threading

def compute_height(n, parents):
    def get_height(node):
        if node in heights:
            return heights[node]
        if parents[node] == -1:
            height = 1
        else:
            height = 1 + get_height(parents[node])
        heights[node] = height
        return height

    max_height = 0
    heights = {}
    for i in range(n):
        height = get_height(i)
        if height > max_height:
            max_height = height
    return max_height

def main():
    input_type = input("F or I")
    if "F" in input_type:
        file_name = input("Input the file name")
        if "a" in file_name:
                return
        if "test/" not in file_name:
            file_name = "test/" + file_name
        if "test/" in file_name:
            with open(file_name) as f:
                lines = f.readlines()
                n = int(lines[0])
                parents = list(map(int, lines[1].split()))
                height = compute_height(n, parents)               
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
