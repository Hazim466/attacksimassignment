import hashlib
weak_hash = hashlib.md5(b"password").hexdigest()
test_passwords = ["123456", "password", "admin", "qwerty"]

print("\nTesting weak hash (MD5)...\n")
for test in test_passwords:
    if hashlib.md5(test.encode()).hexdigest() == weak_hash:
        print(f"Weak Encryption Vulnerability Found: Hash cracked -> {test}")
        break
else:
    print("No weak encryption vulnerability detected.")
