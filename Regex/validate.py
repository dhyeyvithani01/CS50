import re

email = input("What's your email?\n").strip()

if re.search(r"^(\w|\.)+@(\w|\.)+\.(edu|com|gov|in|us|au|org|net)$",email, re.IGNORECASE):    # \w = [a-zA-Z0-9_]
    print("vaild")
else:
    print("Invaild")