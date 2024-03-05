# Samuel Nerayo
# c3400
# BST in python that stores tree of int
# A tree consists of [value of root node, left subtree, right
# subtree] or zero elements

import sys

#exception for duplicate val
class DuplicateEntry(Exception):
    pass

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
#insert val in a BST recursive function
def insert(tree, value):
    if tree is None: #check if tree is empty
        return Node(value)
    else:
        #raise exception if val exists
        if tree.value == value:
            raise DuplicateEntry("Duplicate value detected: {}".format(value))
        #insert to the right
        elif tree.value < value:
            tree.right = insert(tree.right, value)
        #insert to the left if val is less then the root
        else:
            tree.left = insert(tree.left, value)
        return tree

# BST recursive search function
def search(tree, value):
    if tree is None:
        return False
    elif tree.value == value:
        return True
    elif value < tree.value:
        return search(tree.left, value)
    else:
        return search(tree.right, value)

# inorder traversal recursive function
def inorder(tree):
    if tree.left:
        yield from inorder(tree.left)
    yield tree.value
    if tree.right:
        yield from inorder(tree.right)

#Finding height in BST to store in dict
def height(tree):
    if not tree:
        return {}

    def dfs(node, depth):
        if node:
            result[node.value] = depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

    result = {}
    dfs(tree, 0)
    return result

#Converting BST to list recursively
def tree_to_list(tree):
    if tree is None:
        return []
    else:
        #Adding the root to the left and right recursively
        return [tree.value, tree_to_list(tree.left), tree_to_list(tree.right)]

#Driver function
if __name__ == '__main__':

    #Step 1, To get the name of the input file from command
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Error: Input file name missing.")
        sys.exit(1)

    #Step 2, Read file and create the tree
    tree = None
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                value = int(line)
                tree = insert(tree, value)
            except ValueError:
                print("The line is invalid: {}".format(line))
            except DuplicateEntry as e:
                print(str(e))

    # Step 3, printing the inorder traversal of the tree
    # Step 3, printing the tree
    print("Step 3:")
    print(tree_to_list(tree))

    # Step 4, checking if values are in the tree
    print("Step 4:")
    for i in range(1, 10):
        if search(tree, i):
            print("{} YES".format(i))
        else:
            print("{} NO".format(i))

    # Step 5, printing inorder traversal
    print("Step 5:")
    for node in inorder(tree):
        print(node)

    # Step 6, printing the list of inorder traversal
    print("Step 6:")
    List = [value for value in inorder(tree)]
    print(List)

    # Step 7, printing the dictionary of heights
    print("Step 7:")
    result = height(tree)
    print(result)

    # Step 8, printing the overall height of the tree
    print("Step 8:")
    print(max(result.values()))
