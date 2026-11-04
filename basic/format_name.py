string_to_process = "   sMitH, aLeX    "

# Expected output: "Alex Smith"

cleaned = string_to_process.strip()
last, first = cleaned.split(",")
last = last.strip().capitalize()
first = first.strip().capitalize()
print(f"{first} {last}")