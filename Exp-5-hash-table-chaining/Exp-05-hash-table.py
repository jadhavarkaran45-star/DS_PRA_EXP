class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print("Key updated successfully.")
                return

        self.table[index].append((key, value))
        print("Inserted:", key, value)

    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                print("Value found:", v)
                return v

        print("Key not found.")
        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                print("Deleted:", key)
                return

        print("Key not found.")

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable()

ht.insert(45, "Rohit")
ht.insert(55, "Hitman")
ht.insert(35, "RAJA")
ht.insert(18, "Virat")
ht.insert(28, "King")

ht.search(45)
ht.search(35)
ht.search(9)

ht.delete(55)
ht.delete(18)
ht.delete(72)

ht.display()
