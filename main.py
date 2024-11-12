
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(node):
    if node is None:
        return


    if node.left is None and node.right is None:
        print(node.data)


    if node.left:
        printLeafNodes(node.left)
    if node.right:
        printLeafNodes(node.right)



def countEdges(node):
    if node is None:
        return 0


    left_edges = countEdges(node.left)
    right_edges = countEdges(node.right)

    return 1 + left_edges + right_edges

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)


print("Leaf nodes are:")
printLeafNodes(root)


edges = countEdges(root)
print(f"Total number of edges: {edges}")
