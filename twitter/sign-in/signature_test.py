#!/usr/bin/env python3

import re
import uuid
import time
import hmac
import json
import base64

from hashlib import sha1
from urllib.parse import quote
from http.client import HTTPSConnection

def get_base_url(protocol, host, path):
    return "{}{}{}".format(protocol, host, path)

def get_urlencoded_callback():
    s = "http://127.0.0.1:80/callback"
    return quote(s, safe="")

def get_nonce():
    s = str(uuid.uuid4())
    r = re.sub("[^0-9A-Za-z]", "", s)
    return r

def get_timestamp():
    i = int(time.time())
    return str(i)

def get_signature_base_string(verb, base_url, params_string):
    verb = verb.upper()
    base_url = quote(base_url, safe="")
    params_string = quote(params_string, safe="")

    base = "{}&{}&{}".format(verb, base_url, params_string)
    return base

# signature args
# - does not use callback
# - sort keys lexographically
# - returns list of 2-tuples
# - query string variables belong here as well
def get_signature_params(oauth_args, getting_request_token=True):
    params = list()
    exclude = excluded_signature_params(getting_request_token)

    for k in oauth_args:
        if k in exclude:
            continue
        url_k, url_v = quote(k, safe=""), quote(oauth_args[k], safe="")
        params.append((url_k, url_v))

    params.sort(key=lambda t: t[0])
    return params

def get_signature_params_string(params):
    s = ""
    for (k, v) in params:
        s += k + "=" + v + "&"
    s = s[0:-1]
    return s

# hash and base64 encode
def get_b64_signature(base_string, signing_key):
    # hash_bytes = hmac.new(signing_key, base_string, sha1).digest()
    # b64_hash_bytes = base64.b64encode(hash_bytes)
    # signature = str(b64_hash_bytes, "ascii")
    # return signature
    # return make_digest(base_string, signing_key)
    return quote(base64.standard_b64encode(hmac.new(signing_key.encode(), base_string.encode(), sha1).digest()).decode('ascii'))

# todo : urlencode the components or not
def get_signature_key(consumer_secret, oauth_access_token_secret):
    key = quote(consumer_secret,"") + "&"
    if oauth_access_token_secret:
        key += quote(oauth_access_token_secret, "")
    return key

# todo : is callback used or not
def excluded_signature_params(getting_request_token):
    exclude = ["oauth_signature"]
    if getting_request_token:
        exclude.append("oauth_token")
    return exclude

def excluded_header_params(getting_request_token):
    if getting_request_token:
        exclude = ["oauth_token"]
    else:
        exclude = ["oauth_callback"]
    return exclude

def build_oauth_header(oauth_args, getting_request_token):
    exclude = excluded_header_params(getting_request_token)
    header = "Oauth "

    l = list()
    for k in oauth_args:
        if k in exclude:
            continue
        l.append(quote(k, safe="") + "=\"" + quote(oauth_args[k], safe="") + "\", ")
    l.sort()

    header = header + "".join(l)
    return header[0:-2]

    # for k in oauth_args:
    #     if k in exclude:
    #         continue
    #     header += quote(k, safe="") + "=\"" + quote(oauth_args[k], safe="") + "\", "
    # header = header[0:-2]
    # return header

def make_digest(message, key):
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')
    digester = hmac.new(key, message, sha1)
    signature1 = digester.digest()
    signature2 = base64.urlsafe_b64encode(signature1)
    return str(signature2, 'UTF-8')

# http variables
VERB = "POST"
PROTOCOL = "https://"
HOST = "api.twitter.com"
PATH = "/oauth/request_token"
BASE_URL = get_base_url(PROTOCOL, HOST, PATH)

# oauth header variables - note the header has no oauth_token for a request_token
getting_request_token = True
consumer_secret = "L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg"
oauth_access_token_secret = None

oauth_args = {
    "oauth_callback": "http%3A%2F%2Flocalhost%2Fsign-in-with-twitter%2F",
    "oauth_token": None,
    "oauth_signature": None,
    "oauth_consumer_key": "cChZNFj6T5R0TigYB9yd1w",
    "oauth_nonce": "ea9ec8429b68d6b77cd5600adbbb0456",
    "oauth_timestamp": "1318467427",
    "oauth_version": "1.0",
    "oauth_signature_method": "HMAC-SHA1"
}

# build signature
signature_params = get_signature_params(oauth_args, getting_request_token=getting_request_token)
print("signature params...\n{}\n".format(signature_params))

signature_params_string = get_signature_params_string(signature_params)
print("generated signature parameter string...\n{}\n".format(signature_params_string))

signature_base_string = get_signature_base_string(VERB, BASE_URL, signature_params_string)
print("generated signature base string...\n{}\n".format(signature_base_string))

signature_key = get_signature_key(consumer_secret, oauth_access_token_secret)
print("generated signature key...\n{}\n".format(signature_key))

signature = get_b64_signature(signature_base_string, signature_key)
oauth_args["oauth_signature"] = "F1Li3tvehgcraF8DMJ7OyxO4w9Y%3D"
print("generated oauth signature...\n{}\n".format(signature))

# build oauth header
header = build_oauth_header(oauth_args, getting_request_token)
print("built oauth header...\n{}\n".format(header))

# http request
conn = HTTPSConnection(HOST)
headers = {
    "Authorization":header
}

conn.request(VERB, PATH, headers=headers)
resp = conn.getresponse()
resp_bytes = resp.read()
resp_str = str(resp_bytes, "ascii")
data = json.loads(resp_str)
print(data)
