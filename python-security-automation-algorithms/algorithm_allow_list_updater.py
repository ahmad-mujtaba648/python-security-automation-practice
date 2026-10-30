"""
Allow list updater.

Reads a text file of allowed IP addresses, removes the addresses that
should no longer have access, and saves the updated list back to the file.
"""


def update_file(import_file, remove_list):
    # 1. Open the file in read mode and store its contents as a string
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # 2. Convert the string into a list (split on whitespace)
    ip_addresses = ip_addresses.split()

    # 3. Loop through the remove list and delete each address that is present
    #    (looping over remove_list, not ip_addresses, avoids skipping items
    #    while removing from the list being looped over)
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # 4. Convert the list back into a space-separated string
    ip_addresses = " ".join(ip_addresses)

    # 5. Open the file in write mode and overwrite it with the updated list
    with open(import_file, "w") as file:
        file.write(ip_addresses)


# Verification check
# The last address is not in the file, so it is simply ignored.
remove_list = ["192.168.20.77", "192.168.50.91", "192.168.99.99"]

with open("allow_list.txt", "r") as file:
    before = file.read()
print("Before:")
print(before)

update_file("allow_list.txt", remove_list)

with open("allow_list.txt", "r") as file:
    after = file.read()
print("After:")
print(after)