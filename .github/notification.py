import os

# Environment variables
author = os.getenv('AUTHOR_NAME')
branch_name = os.getenv('BRANCH_NAME')
release_notes = os.getenv('RELEASE_NOTES')
build_result = os.getenv('BUILD_FAILED')
build_error = os.getenv('BUILD_ERROR')

# Create the message to be sent
origin = "Development"
if branch_name == "release/prod-vue3x":
    origin = "Production Environment"
elif branch_name == "release/version-vue3x":
    origin = "Development Environment"

# Create the message to be sent
message = f"""
🎉 **New Release Deployed!**

-------------------

👤 **Released By:**
{author}

🌿 **Branch Name:**
{branch_name}

-------------------

🌐 **Origin:**
{origin}

-------------------

📝 **Release Notes:**
{release_notes}

-------------------

📝 **N.B.:** This message is automatically generated by the CI/CD pipeline to notify you of the latest deployment status. 🚀

Thank you! 🙏
"""


if build_result == "failure":
    message = f"""
    🚨 **Deployment Alert!**

    -------------------

    ❌ **Build Failed**

    👤 **Triggered By:**
    {author}
    
    -------------------

    🌿 **Branch Name:**
    {branch_name}

    -------------------

    📄 **Error Details:**
    {build_error}

    -------------------
    
    🌐 **Origin:**
    {origin}

    -------------------

    📝 **N.B.:** This message is automatically generated by the CI/CD pipeline to notify you of the latest deployment status. 🚀
    
    Please address the issue as soon as possible. Thank you! 🙏
    """

# Function to send the message through Skype bot
# send_skype_message(message)

print(message)
