import base64

USERNAME = "my_user"
PASSWORD = "my_password"

def check_credentials(auth_header):
    if auth_header.startswith("Basic "):
        # Extract and decode the base64-encoded username:password
        auth_value = auth_header.split(" ")[1]
        decoded_value = base64.b64decode(auth_value).decode('utf-8')
        username, password = decoded_value.split(":")

        # Check if the username and password match
        return username == USERNAME and password == PASSWORD
    return False
