import re


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False


def main():
    print("🔹 Email Validation System 🔹")
    while True:
        email = input("\nEnter an email to validate (or type 'exit' to quit): ")

        if email.lower() == "exit":
            print("Exiting program. Goodbye!")
            break

        if is_valid_email(email):
            print(f"✅ '{email}' is a valid email address.")
        else:
            print(f"❌ '{email}' is NOT a valid email address. Please try again.")


if __name__ == "__main__":
    main()