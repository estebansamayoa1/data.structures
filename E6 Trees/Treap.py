from random import randrange
 
 
class TreapNode:
    def __init__(self, data, priority=100, left=None, right=None):
        self.data = data
        self.priority = randrange(priority)
        self.left = left
        self.right = right
 
def rotateLeft(root):
 
    R = root.right
    X = root.right.left
 
    R.left = root
    root.right = X
 
    return R
 
 
 
def rotateRight(root):
    L = root.left
    Y = root.left.right
 
    L.right = root
    root.left = Y
 
    return L
 
 
def insertNode(root, data):
 

    if root is None:
        return TreapNode(data)
 
    if data < root.data:
        root.left = insertNode(root.left, data)
 

        if root.left and root.left.priority > root.priority:
            root = rotateRight(root)
    else:
        root.right = insertNode(root.right, data)
 
        if root.right and root.right.priority > root.priority:
            root = rotateLeft(root)
 
    return root
 
 
def searchNode(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return searchNode(root.left, key)
 
    return searchNode(root.right, key)
 
 

def deleteNode(root, key):
 
    if root is None:
        return None
 
    if key < root.data:
        root.left = deleteNode(root.left, key)
 
    elif key > root.data:
        root.right = deleteNode(root.right, key)
 
    else:
 
        if root.left is None and root.right is None:

            root = None
        elif root.left and root.right:
            if root.left.priority < root.right.priority:
                root = rotateLeft(root)
 
                root.left = deleteNode(root.left, key)
            else:
                root = rotateRight(root)
 
                root.right = deleteNode(root.right, key)
 
        else:
            child = root.left if (root.left) else root.right
            root = child
 
    return root
 
 

def printTreap(root, space):
 
    height = 10
 
    if root is None:
        return
 
    space += height
 
    printTreap(root.right, space)
 
    for i in range(height, space):
        print(' ', end='')
 
    print((root.data, root.priority))
 
    printTreap(root.left, space)
 
 
if __name__ == '__main__':
 

    keys = [5, 2, 1, 4, 9, 8, 10]
 
    root = None
    for key in keys:
        root = insertNode(root, key)
 
    print("Constructed :\n\n")
    printTreap(root, 0)

    print(" Adding node 15:\n\n")
    root = insertNode(root, 15)
    printTreap(root, 0)

 
    print("\nDeleting node 1:\n\n")
    root = deleteNode(root, 1)
    printTreap(root, 0)
 
    print("\nDeleting node 5:\n\n")
    root = deleteNode(root, 5)
    printTreap(root, 0)
 
    print("\nDeleting node 9:\n\n")
    root = deleteNode(root, 9)
 
    printTreap(root, 0)