class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print("Duplicate values are not allowed.")

        return root

    def search(self, root, key):
        if root is None:
            return False

        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


bst = BinarySearchTree()

while True:
    print("\n===== BINARY SEARCH TREE MENU =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter value to insert: "))
        bst.root = bst.insert(bst.root, key)
        print("Insertion completed.")

    elif choice == '2':
        key = int(input("Enter value to search: "))
        if bst.search(bst.root, key):
            print("Element found.")
        else:
            print("Element not found.")

    elif choice == '3':
        key = int(input("Enter value to delete: "))
        if bst.search(bst.root, key):
            bst.root = bst.delete(bst.root, key)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == '4':
        print("Inorder Traversal:")
        bst.inorder(bst.root)
        print()

    elif choice == '5':
        print("Preorder Traversal:")
        bst.preorder(bst.root)
        print()

    elif choice == '6':
        print("Postorder Traversal:")
        bst.postorder(bst.root)
        print()

    elif choice == '7':
        print("Exiting Program.")
        break

    else:
        print("Invalid choice.")
