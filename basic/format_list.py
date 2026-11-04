string_to_process = "eggs,cheese,milk,bread,cereal"

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"

items = string_to_process.upper().split(",")
result = " | ".join(items)
print(result)