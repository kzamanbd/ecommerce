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

print(build_error)
print(deploy_failed)
