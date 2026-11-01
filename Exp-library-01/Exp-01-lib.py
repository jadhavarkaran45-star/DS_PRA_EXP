from collections import Counter

n = int(input("Enter number of library members: "))
borrow = []

for i in range(n):
    count = int(input(f"Enter books borrowed by member {i+1}: "))
    borrow.append(count)

average = sum(borrow) / n
highest = max(borrow)
lowest = min(borrow)
zero = borrow.count(0)

frequency = Counter(borrow)
mode = frequency.most_common(1)[0][0]

print("\n========== LIBRARY REPORT ==========")
print("Borrow Counts:", borrow)
print("Average Borrow Count:", average)
print("Highest Borrow Count:", highest)
print("Lowest Borrow Count:", lowest)
print("Members with No Borrowings:", zero)
print("Most Frequent Borrow Count (Mode):", mode)
