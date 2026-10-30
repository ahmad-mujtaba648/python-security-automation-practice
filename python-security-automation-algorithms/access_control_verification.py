"""
Access control verification.

A login attempt is accepted only if the user is on the approved list
AND the attempt was made during organization hours.
"""

approved_list = ["areeba", "hamza", "sana", "usman", "zainab"]


def check_login(username, organization_hours):
    if username in approved_list and organization_hours == True:
        print("Login attempt made by an approved user during organization hours.")
    else:
        print("Username not approved or login attempt made outside of organization hours.")


# Test cases
print("Approved user, inside hours:")
check_login("hamza", True)

print("Approved user, outside hours:")
check_login("hamza", False)

print("Unknown user, inside hours:")
check_login("guest01", True)