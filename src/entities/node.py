class Node:
    def __init__(self, size = None):
        self.vertical = True
        self.children = []
        self.parent = None
        self.size = size
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self