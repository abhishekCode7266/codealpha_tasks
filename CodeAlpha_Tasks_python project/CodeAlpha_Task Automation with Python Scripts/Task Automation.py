import re
import os

# File names
input_file = "input_emails.txt"
output_file = "extracted_emails.txt"

# Create sample input file only once
if not os.path.exists(input_file):
    with open(input_file, "w", encoding="utf-8") as file:
        file.write("john@gmail.com\n")
        file.write("support@example.com\n")
        file.write("admin@test.org\n")
        file.write("sales@company.com\n")

# Read the file
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Find email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)

# Remove duplicates
emails = sorted(set(emails))

# Save emails
with open(output_file, "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

# Display result
print("\n========== EMAIL EXTRACTOR ==========\n")

for email in emails:
    print(email)

print(f"\nTotal Emails Found : {len(emails)}")
print(f"Output File        : {output_file}")
print("\nTask Completed Successfully!")