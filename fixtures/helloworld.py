
import random

# This metdod returns randomized credentials for productpage
def get_credentials():
    login = ''.join(random.choice('testabcd') for _ in range(6))
    password = ''.join(random.choice('testabcd#12345') for _ in range(10))
    return {
        "username": login,
        "passwd": password
    }