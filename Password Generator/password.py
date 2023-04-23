import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    # Define possible characters for password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(chars) for _ in range(int(length_entry.get())))

    # Update the label with the generated password
    password_label.config(text=password)

def copy_password():
    # Get the password from the label
    password = password_label.cget("text")

    # Copy the password to the clipboard
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")

# Create label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Create label to display generated password
password_label = tk.Label(root, text="")
password_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create button to copy password to clipboard
copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()