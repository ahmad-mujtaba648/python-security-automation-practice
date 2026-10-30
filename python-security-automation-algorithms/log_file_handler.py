"""
Log file handler.

Appends a missing entry to the login log file. It adds a new line first if
needed, and skips the entry if it is already in the file, so running the
script again does not create duplicates.
"""

import_file = "login.txt"
missing_entry = "zainab,192.168.30.64,16:42:10,2026-10-12"

# Read the current contents first
with open(import_file, "r") as file:
    text = file.read()

if missing_entry in text:
    print("Entry already present, nothing to append.")
else:
    with open(import_file, "a") as file:
        # Start on a new line if the file does not already end with one
        if text != "" and text[-1] != "\n":
            file.write("\n")
        file.write(missing_entry + "\n")

with open(import_file, "r") as file:
    text = file.read()

print("Login file updated:")
print(text)