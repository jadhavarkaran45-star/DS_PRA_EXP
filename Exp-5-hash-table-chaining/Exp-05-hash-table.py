TABLE_SIZE = 10

hash_table = [[] for _ in range(TABLE_SIZE)]

def hash_function(key):
    return key % TABLE_SIZE

def insert(key, value):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key already exists. Value updated.")
            return

    hash_table[index].append([key, value])

    print("Key-value pair inserted successfully.")


def search(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            print("Value found:", pair[1])
            return pair[1]

    print("Key not found.")
    return None


def delete(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Key-value pair deleted successfully.")
            return

    print("Key not found.")


def display():
    print("\n----- HASH TABLE -----")

    for index in range(TABLE_SIZE):
        print(index, ":", hash_table[index])

while True:

    print("\n===== HASH TABLE =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        key = int(input("Enter key: "))
        value = input("Enter value: ")

        insert(key, value)

    elif choice == "2":

        key = int(input("Enter key to search: "))

        search(key)

    elif choice == "3":

        key = int(input("Enter key to delete: "))

        delete(key)

    elif choice == "4":

        display()

    elif choice == "5":

        print("Program ended.")
        break

    else:

        print("Invalid choice.")
