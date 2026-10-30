# Python Security Automation Practice

> Small Python scripts that automate everyday security-analyst tasks: updating an IP allow list, verifying logins, spotting unusual login activity, and keeping a login log tidy.

![Python 3](https://img.shields.io/badge/Python-3-blue)
![Type](https://img.shields.io/badge/type-practice%20project-lightgrey)
![Course](https://img.shields.io/badge/course-Automate%20Cybersecurity%20Tasks%20with%20Python-green)

## Table of Contents

1. [Overview](#overview)
2. [Quick start](#quick-start)
3. [What is inside](#what-is-inside)
4. [Skills demonstrated](#skills-demonstrated)
5. [Scripts in detail](#scripts-in-detail)
6. [Data files](#data-files)
7. [Testing notes](#testing-notes)
8. [Design decisions](#design-decisions)
9. [What I learned](#what-i-learned)
10. [Limitations and roadmap](#limitations-and-roadmap)
11. [About this project](#about-this-project)
12. [Author](#author)

---

## Overview

This repository contains four short Python scripts, each solving one small but realistic security task:

- keeping an **IP allow list** up to date,
- checking that a login is allowed (approved user **and** working hours),
- flagging **unusual login activity** and locking an account when no attempts remain,
- adding a missing entry to a **login log** without breaking the file.

They are practice programs, not production tools. The goal was to take what I learned in the course and use it together on tasks that look like real security work.

### Why I built this

While studying **Course 7: Automate Cybersecurity Tasks with Python** (Google Cybersecurity Certificate), I wanted to go beyond the guided labs. I rebuilt the ideas as small scripts with my own sample data, ran each one more than once, and fixed the problems I found. For example, one script was adding the same log entry again on every run, so I changed it to check first.

---

## Quick start

**Requirements:** Python 3. No extra libraries are needed.

1. Download this repository (green **Code** button, then **Download ZIP**) or clone it.
2. Open the folder in a terminal or in VS Code.
3. Run any script:

```bash
python algorithm_allow_list_updater.py
python access_control_verification.py
python login_anomaly_detector.py
python log_file_handler.py
```

> **Note:** Two scripts change their data file. The first run edits `allow_list.txt` and `login.txt`; later runs make no further change. To get the original sample data back, copy the original text from the [Data files](#data-files) section into the two files again (or run `git restore allow_list.txt login.txt` if you cloned the repository).

---

## What is inside

| File | Type | Purpose |
|---|---|---|
| `algorithm_allow_list_updater.py` | Script | Removes IP addresses on a remove list from the allow list file |
| `access_control_verification.py` | Script | Accepts a login only for an approved user during organization hours |
| `login_anomaly_detector.py` | Script | Compares today's logins with the daily average and checks remaining attempts |
| `log_file_handler.py` | Script | Appends a missing entry to the login log without duplicates |
| `allow_list.txt` | Data | Sample allow list (space-separated IP addresses) |
| `login.txt` | Data | Sample login log (CSV format) |
| `screenshots/` | Images | Screenshots of each script's output |

### Project structure

```
python-security-automation-practice/
└── screenshots/
    ├── scr-shot-1.png
    ├── scr-shot-2.png
    ├── scr-shot-3.png
    └── scr-shot-4.png
├── access_control_verification.py
├── algorithm_allow_list_updater.py
├── allow_list.txt
├── log_file_handler.py 
├── login.txt
├── login_anomaly_detector.py
└── README.md
```

---

## Skills demonstrated

| Skill | Python concepts used | Where |
|---|---|---|
| File handling | `open()`, `with`, modes `"r"` / `"w"` / `"a"`, `.read()`, `.write()` | updater, log handler |
| Parsing data | `.split()`, `.join()`, `.remove()` | updater |
| Decision making | `if` / `else`, `and`, `in`, comparison operators | updater, access control, anomaly detector, log handler |
| Loops | `for` loop over a list | updater |
| Functions | parameters, `return`, calling a function | updater, access control, anomaly detector |
| Defensive checks | zero-division check, duplicate-entry check, new-line check | anomaly detector, log handler |
| Readable code | comments, docstrings, 4-space indentation (PEP 8) | all scripts |

---

## Scripts in detail

### 1. Allow list updater

**File:** `algorithm_allow_list_updater.py`

Reads `allow_list.txt`, removes every IP address that appears on a remove list, and saves the updated list back to the same file.

| Step | What happens | Python concept |
|---|---|---|
| 1 | Open the file in read mode and store its contents as a string | `with open(..., "r")`, `.read()` |
| 2 | Convert the string into a list of IP addresses | `.split()` |
| 3 | Loop through the remove list and delete each address that is present | `for`, `if ... in`, `.remove()` |
| 4 | Convert the list back into one space-separated string | `" ".join(...)` |
| 5 | Open the file in write mode and overwrite it | `with open(..., "w")`, `.write()` |
| 6 | Print the file before and after to verify the result | `print()` |

**Output (first run):**

![Output of algorithm_allow_list_updater.py](assets/scr-shot-1.png)


*Screenshot: `scr-shot-1.png`*

```
Before:
192.168.10.21 192.168.10.35 192.168.20.14 192.168.20.77 192.168.30.8 192.168.30.64 192.168.40.19 192.168.40.52 192.168.50.3 192.168.50.91
After:
192.168.10.21 192.168.10.35 192.168.20.14 192.168.30.8 192.168.30.64 192.168.40.19 192.168.40.52 192.168.50.3
```

Two addresses were removed. The third address on the remove list (`192.168.99.99`) is not in the file, so it is ignored.

---

### 2. Access control verification

**File:** `access_control_verification.py`

A login attempt is accepted only if the user is on the approved list **and** the attempt was made during organization hours.

| Step | What happens | Python concept |
|---|---|---|
| 1 | Store the approved usernames in a list | list |
| 2 | Define `check_login(username, organization_hours)` | function, parameters |
| 3 | Check that the user is in the list and the hours flag is `True` | `in`, `and`, `==` |
| 4 | Print an accepted or rejected message | `if` / `else`, `print()` |
| 5 | Test three cases: approved inside hours, approved outside hours, unknown user | function calls |

**Output:**

![Output of access_control_verification.py](assets/scr-shot-4.png)

*Screenshot: `scr-shot-4.png`*

```
Approved user, inside hours:
Login attempt made by an approved user during organization hours.
Approved user, outside hours:
Username not approved or login attempt made outside of organization hours.
Unknown user, inside hours:
Username not approved or login attempt made outside of organization hours.
```

---

### 3. Login anomaly detector

**File:** `login_anomaly_detector.py`

Two small monitoring checks:

1. **Login ratio:** compares today's logins with the user's daily average and raises an alert at 3 times the average or more.
2. **Remaining attempts:** locks the account when no login attempts are left.

| Step | What happens | Python concept |
|---|---|---|
| 1 | `analyze_logins()` divides today's logins by the average and returns the ratio | function, `return`, division |
| 2 | If the ratio is 3 or more, print an alert | `if`, `>=` |
| 3 | If the average is 0, print a message instead of dividing | `if` / `else`, `==` |
| 4 | `remaining_login_attempts()` returns maximum attempts minus attempts used | function, `return` |
| 5 | If no attempts remain, print "Your account is locked" | `if`, `<=` |

**Output:**

![Output of login_anomaly_detector.py](assets/scr-shot-2.png)


*Screenshot: `scr-shot-2.png`*

```
Current day login total for sana is 9
Average logins per day for sana is 3
Alert! This account has more login activity than normal.

No login history for newuser - ratio cannot be calculated.

Your account is locked
```
  
---

### 4. Log file handler

**File:** `log_file_handler.py`

Adds a missing entry to `login.txt`. It checks first, so running the script again does not create duplicates.

| Step | What happens | Python concept |
|---|---|---|
| 1 | Read the current contents of the log file | `with open(..., "r")`, `.read()` |
| 2 | If the entry is already in the file, print a message and stop | `if ... in` |
| 3 | Otherwise open the file in append mode | `with open(..., "a")` |
| 4 | Start a new line first if the file does not end with one | `text[-1] != "\n"` |
| 5 | Write the entry followed by a new line | `.write()`, string concatenation |
| 6 | Read the file again and print it to confirm the result | `.read()`, `print()` |

**Output (first run):**


![Output of log_file_handler.py](assets/scr-shot-3.png)

*Screenshot: `scr-shot-3.png`*

```
Login file updated:
username,ip_address,time,date
areeba,192.168.10.21,9:15:02,2026-10-12
hamza,192.168.20.14,11:40:37,2026-10-12
sana,192.168.30.8,14:05:19,2026-10-12
usman,192.168.40.19,8:52:44,2026-10-12
zainab,192.168.30.64,16:42:10,2026-10-12
```

**Output (second run):** the entry is already there, so nothing is added.

```
Entry already present, nothing to append.
Login file updated:
username,ip_address,time,date
areeba,192.168.10.21,9:15:02,2026-10-12
hamza,192.168.20.14,11:40:37,2026-10-12
sana,192.168.30.8,14:05:19,2026-10-12
usman,192.168.40.19,8:52:44,2026-10-12
zainab,192.168.30.64,16:42:10,2026-10-12
```

---

## Data files

All names, IP addresses and log entries are **fictional sample data**.

| File | Format |
|---|---|
| `allow_list.txt` | One line, IP addresses separated by spaces |
| `login.txt` | CSV: `username,ip_address,time,date` with a header row |

**Original `allow_list.txt`:**

```
192.168.10.21 192.168.10.35 192.168.20.14 192.168.20.77 192.168.30.8 192.168.30.64 192.168.40.19 192.168.40.52 192.168.50.3 192.168.50.91
```

**Original `login.txt`:**

```
username,ip_address,time,date
areeba,192.168.10.21,9:15:02,2026-10-12
hamza,192.168.20.14,11:40:37,2026-10-12
sana,192.168.30.8,14:05:19,2026-10-12
usman,192.168.40.19,8:52:44,2026-10-12
```

---

## Testing notes

I ran every script and compared its output with what I expected. The two scripts that edit files were run twice, because a bug can hide on the second run.

| Script | What I checked | Result |
|---|---|---|
| Allow list updater | Addresses on the remove list disappear from the file | Pass |
| Allow list updater | An address that is not in the file is ignored | Pass |
| Allow list updater | Running it a second time changes nothing | Pass |
| Access control verification | Approved user inside hours is accepted | Pass |
| Access control verification | Approved user outside hours, and unknown user, are rejected | Pass |
| Login anomaly detector | 9 logins against an average of 3 raises an alert | Pass |
| Login anomaly detector | An average of 0 prints a message instead of crashing | Pass |
| Log file handler | The entry is added on its own line | Pass |
| Log file handler | Running it a second time does not add a duplicate | Pass |

---

## Design decisions

| Decision | Reason |
|---|---|
| The updater loops over `remove_list`, not the allow list | Removing items from a list while looping over the same list can make Python skip the next item |
| The log handler checks before appending | Without the check, every run adds the same entry again |
| The log handler adds a new line only when needed | Otherwise two entries can end up glued on one line |
| A zero average is checked before dividing | Dividing by zero raises a `ZeroDivisionError` |
| `with` is used for every file | The file is closed automatically, even if an error happens |
| Sample data is fictional | No real names or addresses are exposed |

---

## What I learned

- How to open, read, write and append to text files safely with `with`, and why `"w"` replaces a file while `"a"` adds to it.
- How `.split()` and `.join()` convert between a string and a list, so file contents can be processed in a loop and written back.
- How to combine loops, conditionals and functions into a small algorithm that solves a real task.
- How to find bugs by running a script more than once and checking the data file after each run, not only the printed output.
- Why readable code matters: clear names, comments and consistent indentation make a script easier to check and fix.

---

## Limitations and roadmap

### Current limitations

- File names and values are written inside the scripts.
- There are no automated tests; checks were done by running the scripts.
- The scripts assume well-formed input and do not validate IP addresses.
- The login log is treated as plain text, not parsed field by field.

### Roadmap

- [x] Update an allow list from a remove list
- [x] Verify logins with approved users and working hours
- [x] Flag unusual login activity with a ratio check
- [x] Append to a log file without duplicates
- [ ] Take file names and values as command-line arguments
- [ ] Validate IP addresses with regular expressions (`re`)
- [ ] Extract IP addresses from raw log files
- [ ] Read the login log with the `csv` module
- [ ] Add automated tests

---

## About this project

This project was built while studying **Course 7: Automate Cybersecurity Tasks with Python**, part of the **Google Cybersecurity Certificate** on Coursera. The scripts are practice work for learning purposes and are not meant for use in a real security environment.

---

## Author

**Ahmad Mujtaba**

- GitHub: [ahmad-mujtaba648](https://github.com/ahmad-mujtaba648)
- LinkedIn: [Ahmad Mujtaba](https://www.linkedin.com/in/ahmad-mujtaba-9b2539362)
