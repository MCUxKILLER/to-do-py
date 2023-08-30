password = input("Enter new password: ")
result = []
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
upperCase = False
for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        upperCase = True

result.extend((digit, upperCase))
if all(result):
    print("Strong Password.")
else:
    print("Weak password.")
