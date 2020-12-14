import base64
import hashlib
import os
import time
from typing import *
import requests


def basic_token_and_hex_string() -> Tuple[str, str]:
    # You can get these values off jailbroken devices and the like, thanks to yulkytulky for these.
    client_id = 'JuiUH&3822'
    client_secret = 'HuUIC(ZQ918lkl*7'

    # Generate a random number to act as the "ID" for the device.
    hex_string = os.urandom(32).hex()

    # Do a bunch of boring maths to get it into the form ifunny use.
    hex_id = hex_string + '_' + client_id
    hash_decoded = hex_string + ':' + client_id + ':' + client_secret
    hash_encoded = hashlib.sha1(hash_decoded.encode('utf-8')).hexdigest()

    # Return both the hex string and the basic token as both are required for registering tokens.
    return hex_string, base64.b64encode(bytes(hex_id + ':' + hash_encoded, 'utf-8')).decode()


def registered_basic_token() -> str:
    # Generate a normal basic token and hexstring.
    hex_string, basic_token = basic_token_and_hex_string()

    # This is where it gets kinda interesting, to create accounts you have to create "registered" basic tokens,
    # this simply just means making these two requests with the hex string and the tokens and waiting 30 seconds.
    # Its only needed if you want to generate accounts everything else will be fine without it.
    # There is no rate limit on any of these requests so you can generate as many as you want.
    requests.get("https://geoip.ifunny.co/", cookies={
        "device_id": hex_string
    })
    requests.get("https://api.ifunny.mobi/v4/digests/fresh?comments=1", headers={
        "Authorization": "Basic " + basic_token
    })

    # Sleep the required 30 seconds for ifunny to register the token.
    time.sleep(30)
    return basic_token

