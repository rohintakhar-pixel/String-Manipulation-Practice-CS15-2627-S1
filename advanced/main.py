while True:
 print("Choose how you would like to process a string:")
 print()
 print("1. Format a Name")
 print("2. Format a Title")
 print("3. Format a List")
 print("4. Process Numbers")
 print()
 choice = input("Enter your choice: ")

 if choice == "1":
  string_to_process = input("Enter the string to process: ")
  try:
   cleaned = string_to_process.strip()
   last, first = cleaned.split(",")
   last = last.strip().capitalize()
   first = first.strip().capitalize()
   print()
   print("Processed String:")
   print(f"{first} {last}")
  except ValueError:
   print()
   print("That is not a valid name. Please enter it as: Last, First")

 elif choice == "2":
  string_to_process = input("Enter the string to process: ")
  cleaned = string_to_process.replace("::", ",")
  words = cleaned.split(",")

  no_spaces = []
  for word in words:
   no_spaces.append(word.replace(" ", ""))

  result = " ".join(no_spaces).title()
  print()
  print("Processed String:")
  print(result)

 elif choice == "3":
  string_to_process = input("Enter the string to process: ")
  items = string_to_process.upper().split(",")
  result = " | ".join(items)
  print()
  print("Processed String:")
  print(result)

 elif choice == "4":
  string_to_process = input("Enter the string to process: ")
  try:
   cleaned = string_to_process.strip()
   parts = cleaned.split(",")

   numbers = []
   for part in parts:
    numbers.append(int(part.strip()))

   total = sum(numbers)
   average = total / len(numbers)
   print()
   print(f"Total: {total}")
   print(f"Average: {average}")
  except ValueError:
   print()
   print("That is not a valid list of numbers. Please use numbers separated by commas.")

 else:
  print()
  print("Invalid choice. Please enter 1, 2, 3, or 4.")

 print()
 again = input("Process another string? (y/n): ")
 print()
 if again.lower() != "y":
  break
