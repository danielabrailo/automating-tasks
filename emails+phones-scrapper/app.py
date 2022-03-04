import re, pyperclip

# Regex for phone numbers in Israel

phoneRegex = re.compile(r'''
#area code
(((\d\d\d)|(\(\d\d\d\)))?
#first separator
(\s|-)
#frst 3 digits
\d\d\d
#separator
-
#last 4 digits
\d\d\d\d
#extension (optional)
(((ext(\.)?\s)|x)  (\d{2, 5}))?)
''', re.VERBOSE)

# Regex for email
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

text = pyperclip.paste()

# Extracting the emails + phone numbers from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy all to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)