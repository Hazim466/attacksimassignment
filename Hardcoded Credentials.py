hardcoded_password = "Akshay@2332"
potential_passwords = ["password123", "admin123", "Akshay@2332", "test"]

print("Testing hardcoded credentials...\n")
for password in potential_passwords:
    if password == hardcoded_password:
        print(f"Vulnerability Found: Hardcoded password matched -> {password}")
        break
else:
    print("No vulnerability detected for hardcoded password brute force.")
