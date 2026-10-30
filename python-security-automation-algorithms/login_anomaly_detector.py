"""
Simple login monitoring checks.

1. analyze_logins(): compares today's logins with the user's daily average.
2. remaining_login_attempts(): returns how many login attempts are left.
"""


def analyze_logins(username, current_day_logins, average_day_logins):
    # average_day_logins must be greater than 0 (dividing by 0 gives an error)
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins
    return login_ratio


def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts


# 1. Login ratio analysis and alert
login_analysis = analyze_logins("sana", 9, 3)

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")

print()

# A user with no login history: check the average before dividing
average_logins = 0

if average_logins == 0:
    print("No login history for newuser - ratio cannot be calculated.")
else:
    analyze_logins("newuser", 4, average_logins)

print()

# 2. Remaining login attempts check
remaining_attempts = remaining_login_attempts(3, 3)

if remaining_attempts <= 0:
    print("Your account is locked")