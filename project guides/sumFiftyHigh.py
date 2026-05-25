numbers = [32, 42, 88, 48, 72, 25, 61, 97]

sum = 0

for number in numbers:
    if number >= 50:
        sum += number

print(f"The count is {sum}")

print("\\")

for i in range(len(numbers)):
    if (i % 2 != 0):
        print(numbers[i])

print("\\")