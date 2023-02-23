import sys
import threading

def compute_height(n, parents):
    # Initialize max height to 0 and height list to all zeros
    max_height = 0
    height_list = [0] * n

    # Traverse the tree and compute height for each node
    for i in range(n):
        node_height = 1
        j = parents[i]

        # If parent has a computed height, use it to compute height of the current node
        if j != -1 and height_list[j] != 0:
            node_height = height_list[j] + 1
        else:
            # Traverse ancestors of the current node to compute height
            while j != -1 and height_list[j] == 0:
                node_height += 1
                j = parents[j]
            if j != -1:
                node_height += height_list[j]

        # Update max height and height list for the current node
        max_height = max(max_height, node_height)
        height_list[i] = node_height

    return max_height

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute and print max height
    max_height = compute_height(n, parents)
    print(max_height)

# Increase recursion limit and stack size for large test cases
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
