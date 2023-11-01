from dotenv import dotenv_values

def get_token():
    env = dotenv_values()
    token = env.get("TOKEN")
    return token