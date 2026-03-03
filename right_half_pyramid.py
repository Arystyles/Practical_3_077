# Right Half Pyramid Pattern
# Inverted Right Half Pyramid Pattern

rows = 6

for i in range(1, rows + 1):
    print("* " * i)


row = 5
num = 1

for i in range(row, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
        
        # Reset number after 9 (to match given pattern)
        if num == 10:
            num = 1
    print()
