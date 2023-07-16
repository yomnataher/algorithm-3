class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.leftSize = 0

def insert(root, data):
    if root is None:
        return Node(data)
    if data <= root.data:
        root.left = insert(root.left, data)
        root.leftSize += 1
    else:
        root.right = insert(root.right, data)
    return root

def getIndex(root, x):
    if root.data == x:
        return root.leftSize + 1
    if x < root.data:
        if root.left is None:
            return -1
        else:
            return getIndex(root.left, x)
    else:
        if root.right is None:
            return -1
        else:
            rightSize = getIndex(root.right, x)
            if rightSize == -1:
                return -1
            else:
                return root.leftSize + 2 + rightSize

#main
queries = []
Q = int(input())
root = None
for i in range(0,Q):
    query = str(input())
    queries.append(query)

for i in range(0,Q):
    spliter = queries[i].split(" ")
    q = int(spliter[0])
    x = int(spliter[1])
    if q == 1:
        root = insert(root, x)
    elif q == 2:
        print(getIndex(root, x), end=" ")