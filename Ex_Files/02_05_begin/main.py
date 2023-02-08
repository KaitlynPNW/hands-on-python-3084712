
import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT) #grab things from the enviroment; will default to development if no current enviroment

if current_env == DEVELOPMENT: #checking
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]: #checking against multiple things
    print("Codespace or local environment")
else:
    print("Unknown environment")
