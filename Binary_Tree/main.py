# Class for the nodes
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# class for tree
class Tree:
    def __init__(self):
        self.root = None
    
    # method to obtain the value
    def get_root(self):
        return self.root
    
    # method to add value to a node
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)
    
    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    
    # method to find the data
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None
    
    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)
    
    # method for deleting tree
    def delete_tree(self):
        self.root = None
    
    # method to print the tree
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + " ")
            self._print_tree(node.right)

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.print_tree()