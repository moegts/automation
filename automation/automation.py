import re

with open('./assets/potential-contacts.txt')as f:
    potentials = f.read()

## PHONE 📞

phone = []

phone.extend(re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', potentials))

phoneNoDuplicates = list(set(phone))

phoneOrdered = phoneNoDuplicates.sort()

phoneNumString = ''
for num in phoneNoDuplicates:
    phoneNumString += num + "\n"


with open("./phone_numbers.txt", 'w')as f:
    phoneNums = f.write(phoneNumString)

print(phoneNumString)

## EMAIL 📧

email = []
email.extend(re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', potentials))

emailNoDuplicates = list(set(email))
mailOrdered = emailNoDuplicates.sort()

emailString = ''
for email in emailNoDuplicates:
    emailString += email + "\n"

print(emailString)


with open("./emails.txt", 'w') as f:
    emails = f.write(emailString)

