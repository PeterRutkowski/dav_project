class node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()

    def insert(self, value):
        if self.val:
            if value < self.val:
                if self.left is None:
                    self.left = node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = node(value)
                else:
                    self.right.insert(value)
        else:
            self.val=value


tree = node(5)
tree.insert(6)
tree.insert(3)
tree.print()