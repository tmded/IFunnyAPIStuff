import requests


def req_auth_token(btoken: str, email: str, password: str):
    # This endpoint is really basic it basically just does what it says on the tin.
    r = requests.post("https://api.ifunny.mobi/v4/oauth2/token", headers={
        "Authorization": "Basic " + btoken
    }, data={
        "grant_type": "password",
        "username": email,
        "password": password
    })

    # This returns a dict with all the info about the token you need.
    return r.json()