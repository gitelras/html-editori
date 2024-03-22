class Node:
    def __init__(self, children=None):
        self.vertical = True
        self.children = children if children else []
    
