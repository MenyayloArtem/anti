from helpers.get_token import get_token

def get_headers():
    token = get_token()
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type" : "application/json"
    }

    return headers