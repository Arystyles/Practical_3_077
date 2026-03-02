# Even numbers from 1 to 100

even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers:", even_numbers)
print("Minimum:", min(even_numbers))
print("Maximum:", max(even_numbers))
print("Total sum:", sum(even_numbers))
