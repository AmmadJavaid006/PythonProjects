import re

# Function to update the password for a specific site
def update_password(text, site, new_password):
    # Regular expression pattern to find the specific site's password
    pattern = rf"(Website:\s*{re.escape(site)}\s*Password:\s*)([\w@!]+)"
    
    # Replace the old password with the new one
    updated_text = re.sub(pattern, r"\1" + new_password, text)
    
    return updated_text

# Variables
site = "Facebook"
new_password = "newFacebookPassword"

# Read the content from the file
with open('passwords.txt', 'r') as file:
    text = file.read()

# Update the password
updated_text = update_password(text, site, new_password)

# Write the updated content back to the file
with open('updated_passwords.txt', 'w') as file:
    file.write(updated_text)

# For demonstration, printing the updated text
print(updated_text)
