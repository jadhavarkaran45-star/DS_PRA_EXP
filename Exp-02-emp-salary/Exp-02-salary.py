def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries


def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries


n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    salary = float(input("Enter salary of employee " + str(i + 1) + ": "))
    salaries.append(salary)


selection_salaries = salaries.copy()
bubble_salaries = salaries.copy()

selection_sorted = selection_sort(selection_salaries)
bubble_sorted = bubble_sort(bubble_salaries)

top_five = sorted(salaries, reverse=True)[:5]


print("\nOriginal Salaries:")
print(salaries)

print("\nSelection Sort Salaries:")
print(selection_sorted)

print("\nBubble Sort Salaries:")
print(bubble_sorted)

print("\nTop Five Highest Salaries:")
for salary in top_five:
    print(salary)
