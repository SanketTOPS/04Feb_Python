import re

# sanket@gmail.com
email = input("Enter an Email:")

email_ptrn = "[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]"

x = re.findall(email_ptrn, email)

if x:
    print("Valid Email!")
else:
    print("Error!Invalid Email...")
