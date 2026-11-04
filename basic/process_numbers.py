string_to_process = "  18,27,35,20  "

# Expected Output:
# "Total: 100"
# "Average: 25.0"

cleaned = string_to_process.strip()
parts = cleaned.split(",")

numbers = []
for part in parts:
 numbers.append(int(part))

total = sum(numbers)
average = total / len(numbers)

print(f"Total: {total}")
print(f"Average: {average}")