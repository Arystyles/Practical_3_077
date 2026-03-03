# Even numbers from 1 to 100

even_number = []

for i in range(1, 101):
    if i % 2 == 0:
        even_number.append(i)

print("Even numbers:", even_number)
print("Minimum:", min(even_number))
print("Maximum:", max(even_number))
print("Total sum:", sum(even_number))


even_numbers = list(range(2, 51, 2))

print("Even numbers between 1 and 50:", even_numbers)

print("Total of three minimum even numbers:", sum(even_numbers[:3]))

print("Total of three maximum even numbers:", sum(even_numbers[-3:]))

print("Average of even numbers between 1 and 50:", sum(even_numbers) / len(even_numbers))