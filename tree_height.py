# python3
import os
import sys
import threading

def input_read():
    source = input().lower()
    if source == 'i':
        print("Enter nr. of nodes")
        n = int(input())
        print("Parents of nodes")
        parents = list(map(int, input().split()))
        return n, parents
    elif source == 'f':
        while True:
            print("file name")
            filename = input()
            if 'a' in filename:
                print("Cant contain 'a'")
            elif not os.path.isfile('inputs/' + filename):
                print("File not found")
            else:
                with open('inputs/' + filename, "r") as file:
                    n = int(file.readlines().strip())
                    parents = list(map(int, file.readline().strip().split()))
                    return n, parents
    else:
        print("Invalid")
        return input_read()

def build_tree(n, parents):
    # Initialize an empty adjacency list for each node
    adj = [[] for _ in range(n)]

    # Build the adjacency list
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj[parents[i]].append(i)

    return root, adj

print("Input")
def height(root, adj):
    if not adj[root]:
        return 1
    else:
        max_child_height = 0
        for child in adj[root]:
            child_height = height(child, adj)
            if child_height > max_child_height:
                max_child_height = child_height
        return max_child_height + 1


n = int(input())
parents = list(map(int, input().split()))

root, adj = build_tree(n, parents)
tree_height = height(root, adj)

print("Output:")
print(tree_height)

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
threading.Thread(target=height).start()
