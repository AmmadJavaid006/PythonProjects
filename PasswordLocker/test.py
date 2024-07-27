import re

def update_password(file_path, website, new_password):
    # Step 1: Read the file contents
    with open(file_path, 'r') as file:
        contents = file.read()

    # Step 2: Create a regex pattern to find and replace the password
    pattern = rf"(Website:\s*{re.escape(website)}\s*Password:\s*)([\w@!]+)"
    print(f"Pattern: {pattern}")  # Debugging line to check the pattern
    
    # Perform the replacement
    new_contents, num_replacements = re.subn(pattern, rf"\1{new_password}", contents)
    print(f"Number of replacements made: {num_replacements}")  # Debugging line to check replacements
    
    if num_replacements > 0:
        # Step 3: Write the updated contents back to the file
        with open(file_path, 'w') as file:
            file.write(new_contents)
        print(f"Password for {website} has been updated to {new_password}.")
    else:
        print(f"Website {website} not found in the file.")

# User inputs
site = input("Enter the website name: ")
new_password = input("Enter the new password: ")

# Call the function to update the password
update_password('Passwords.txt', site, new_password)

# Debugging: Print the final contents of the file
print("Final file contents:")
with open('Passwords.txt', 'r') as file:
    print(file.read())
