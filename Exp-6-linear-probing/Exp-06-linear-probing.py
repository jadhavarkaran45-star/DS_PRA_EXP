class HashTable:
    def __init__(self):
        self.size = 7
        self.table = [None] * self.size
        self.DELETED = "DELETED"

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index] == key:
                print("Key already exists.")
                return

            index = (index + 1) % self.size

            if index == start_index:
                print("Hash Table is full.")
                return

        self.table[index] = key
        print("Inserted:", key)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print("Key found at index:", index)
                return index

            index = (index + 1) % self.size

            if index == start_index:
                break

        print("Key not found.")
        return -1

    def delete(self, key):
        index = self.search(key)

        if index != -1:
            self.table[index] = self.DELETED
            print("Deleted:", key)

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable()

while True:
    print("\n===== HASH TABLE MENU =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key: "))
        ht.insert(key)

    elif choice == '2':
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif choice == '3':
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == '4':
        ht.display()

    elif choice == '5':
        print("Exiting Program.")
        break

    else:
        print("Invalid choice.")
