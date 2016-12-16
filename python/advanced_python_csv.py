import sys
storage = {}
execfile("advanced_python_regex.py", storage)
emails = storage['email_list']
orig = sys.stdout
with open("emails.csv", "wb") as f:
    sys.stdout = f
    for email in emails:
      print(email)

    sys.stdout = orig
