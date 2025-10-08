users = {
    "alice": {"age": 25, "email": "alice@example.com", "active": True},
    "bob": {"age": 30, "email": "bob@example.com", "active": False},
}

print(users["alice"]["email"])  # direct access

if "alice" in users:
    print("Alice exists!", users["alice"]["email"])
else:
    print("Alice not found.")

print("Usernames:")
for username in users:
    print(" -", username)

print("User infos:")
for info in users.values():
    print(" -", info)
