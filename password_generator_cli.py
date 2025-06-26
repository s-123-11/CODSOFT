# password_generator.py
import random
print("--- PASSWORD GENERATOR! ---")
length = int(input("Enter the length of the password: "))
use_special = input("Include special characters? (yes/no): ").lower()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

all_chars = letters + numbers

if use_special == "yes":
    all_chars += special

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Generated Password:", password)

