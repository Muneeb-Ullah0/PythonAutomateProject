import re

email_condition = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$"

user_email = input("Enter user email ID: ")


if re.match(email_condition, user_email):
    print("✅ Valid Email")
else:
    print("❌ Invalid Email")







