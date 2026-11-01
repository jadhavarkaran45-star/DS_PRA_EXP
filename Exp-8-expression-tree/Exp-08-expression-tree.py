class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ExpressionTree:

    def construct_tree(self, prefix):
        stack = []

        for char in reversed(prefix):
            if char.isalnum():
                node = Node(char)
                stack.append(node)

            else:
                node = Node(char)

                node.left = stack.pop()
                node.right = stack.pop()

                stack.append(node)

        return stack.pop()

    def postorder(self, root):
        if root is None:
            return

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        print("Postorder Traversal:", end=" ")

        while stack2:
            print(stack2.pop().data, end=" ")

        print()

    def delete_tree(self, root):
        if root is None:
            return

        self.delete_tree(root.left)
        self.delete_tree(root.right)

        root.left = None
        root.right = None
        root.data = None


tree = ExpressionTree()

prefix = input("Enter Prefix Expression: ")

root = tree.construct_tree(prefix)

print("\nExpression Tree Constructed Successfully.")

tree.postorder(root)

tree.delete_tree(root)
root = None

print("Expression Tree Deleted Successfully.")
