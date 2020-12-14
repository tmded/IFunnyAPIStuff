import random
import string
from typing import *
import requests
import bearertokengeneration


def generate_account(basictoken: str) -> Optional[Dict[str, Union[str, Any]]]:
    # Generate some random account details.
    email = "".join([random.choice(string.ascii_letters) for i in range(32)]) + "@nerd.loser"
    nick = "".join([random.choice(string.ascii_letters) for i in range(random.randint(12, 15))])
    password = "".join([random.choice(string.ascii_letters) for i in range(14)]) + "28"

    # This is the request that generates accounts, it requires a captcha in everything but v2 of the api.
    # THIS BASIC TOKEN HAS TO BE REGISTERED SEE basictokengeneration.py.
    r = requests.post("https://api.ifunny.mobi/v2/users", headers={
        "Authorization": "Basic " + basictoken,
    }, data={
        "accepted_mailing": "false",
        "email": email,
        "nick": nick,
        "password": password,
        "reg_type": "pwd"
    })

    # Boring error handling.
    if r.status_code != 200:
        return None

    # Here we generate a bearer token for the account so we dont have to generate one next time we use it,
    # this is just for ease of use.
    register = bearertokengeneration.req_auth_token(basictoken, email, password)
    try:
        usertoken = register["access_token"]

    # More Boring error handling.
    except KeyError:
        return None

    return {
        "email": email,
        "password": password,
        "nick": nick,
        "token": usertoken
    }
