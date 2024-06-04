import os

# Retrieve environment variables
author = os.environ.get("AUTHOR_NAME")
branch_name = os.environ.get("BRANCH_NAME")
deploy_failed = os.environ.get("DEPLOY_FAILED")
build_error = os.environ.get("BUILD_ERROR")

print(build_error)
print(deploy_failed)
