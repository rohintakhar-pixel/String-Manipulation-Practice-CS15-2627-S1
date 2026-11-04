string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

# Expected Output: The Tale Of Two Cities

cleaned = string_to_process.replace("::", ",")
words = cleaned.split(",")

no_spaces = []
for word in words:
 no_spaces.append(word.replace(" ", ""))

result = " ".join(no_spaces).title()
print(result)