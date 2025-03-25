import re

# Sanket2020
username = input("Enter an Username:")

unm_pattern = "[A-Z]+[a-z]+[0-9]"

"""try:
    x = re.findall(unm_pattern, username)
    if x:
        print("Username is Valid!")
except Exception as e:
    print(e)
else:
    print("Error!")
"""

try:
    if not re.match(unm_pattern, username):
        raise ValueError("Invalid username format!")
    else:
        print("Username is Valid!")
except Exception as e:
    print(f"Error: {e}")
