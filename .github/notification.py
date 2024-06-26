import os
import requests

# Retrieve environment variables
author_name = os.environ.get("AUTHOR_NAME")
branch_name = os.environ.get("BRANCH_NAME")
release_notes = os.environ.get("RELEASE_NOTES")
build_result = os.environ.get("BUILD_RESULT")
github_run_id = os.environ.get('GITHUB_RUN_ID')
github_actor = os.environ.get('GITHUB_ACTOR')

url = "https://devweb.jerpbd.com/features/users/dashboard"
origin = "Development"
if branch_name == "release/prod-vue3x":
    url = "https://njpl.jerpbd.com/features/users/dashboard"
    origin = "Production Environment"
elif branch_name == "release/version-vue3x":
    origin = "Development Environment"
    
try:
    response = requests.get(f"https://api.github.com/users/{github_actor}")
    data = response.json()
    author_name = data.get("name", author_name)
    print(author_name)
        
except Exception as e:
    print("Failed to fetch author name from GitHub API")
    

# Create the message to be sent
message = f"""
🎉 **New Release Deployed!**

-------------------

👤 **Released By:**
    {author_name}

🌿 **Branch Name:**
    {branch_name}

-------------------

🌐 **Origin:**
    {origin}

-------------------

📝 **Release Notes:**
{release_notes}

-------------------

💻 **More Details:**
    {url}

-------------------

We are excited to announce the successful deployment of the latest release! 🚀

📝 **N.B.:** This message is automatically generated by the CI/CD pipeline to notify you of the latest deployment status. 🚀
Thank you! 🙏
"""

error_message = f"""
🚨 **Deployment Alert!**

-------------------

❌ **Build Failed**

-------------------

👤 **Triggered By:**
    {author_name}

-------------------

🌿 **Branch Name:**
    {branch_name}

-------------------

📄 **Error Details:**
https://github.com/mononsoft/jerp-frontend/actions/runs/{github_run_id}

-------------------

🌐 **Origin:**
    {origin}

-------------------

Please address the issue as soon as possible.

📝 **N.B.:** This message is automatically generated by the CI/CD pipeline to notify you of the latest deployment status. 🚀
Thank you! 🙏
"""

cancelled_message = f"""
🛑 **Deployment Cancelled**

-------------------

❌ **Build Cancelled**

👤 **Triggered By:**
    {author_name}

🌿 **Branch Name:**
    {branch_name}

-------------------

📄 **Error Details:**
https://github.com/mononsoft/jerp-frontend/actions/runs/{github_run_id}

-------------------

The deployment process was cancelled.

📝 **N.B.:** This message is automatically generated by the CI/CD pipeline to notify you of the latest deployment status. 🚀
Thank you! 🙏
"""

if build_result == "failure":
    message = error_message
elif build_result == "cancelled":
    message = cancelled_message

# Function to send the message through Skype bot
print(message)
