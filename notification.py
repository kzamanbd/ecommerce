import os
from skpy import Skype

# Retrieve environment variables
author = os.environ.get("AUTHOR_NAME")
branch_name = os.environ.get("BRANCH_NAME")
username = os.environ.get("SKYPE_USERNAME")
password = os.environ.get("SKYPE_PASSWORD")
release_notes = os.environ.get("RELEASE_NOTES")
build_failed = os.environ.get("BUILD_FAILED")
deploy_failed = os.environ.get("DEPLOY_FAILED")
job_name = os.environ.get("JOB_NAME")
build_error = os.environ.get("BUILD_ERROR")

# Define the Skype recipient and group IDs
group_id = "19:1e55bc9219844d01a3b27253a2f78652@thread.skype"

origin = "Development"
if branch_name == "release/prod-vue3x":
    origin = "Production Environment"
elif branch_name == "release/version-vue3x":
    origin = "Development Environment"

# Create the message to be sent
success_message = f"""
🚀 **Hello!**

This is an automated message generated by a Skype bot and triggered by a GitHub Action. 

---

👤 **Released By:**  
{author}

🌿 **Branch Name:**  
{branch_name}

🌐 **Origin:**  
{origin}

---

📝 **Release Notes:**  
{release_notes}

---

Thank you! 🙏
"""

print(build_error)
print(deploy_failed)

failed_message = f"""
🚨 **Deployment Alert!**

This is an automated message generated by a Skype bot and triggered by a GitHub Action.

---

❌ **Job Failed:**  
{job_name}

👤 **Triggered By:**  
{author}

🌿 **Branch Name:**  
{branch_name}

🌐 **Origin:**  
{origin}

---

📄 **Error Details:**  

---

Please address the issue as soon as possible. Thank you! 🙏
"""

message = success_message

if build_failed == "true":
    message = failed_message
elif deploy_failed == "true":
    message = failed_message

try:
    # Initialize the Skype instance
    # skype = Skype(username, password)
    
    # Send the message to the group
    # chat = skype.chats.chat(group_id)
    # chat.sendMsg(message)
    print(message)

except Exception as e:
    print(f"Failed to send message: {e}")
