# Create Authorization Request

# Based on this documentation
# https://developers.google.com/identity/protocols/oauth2/service-account#python_2 section Addendum
# Authorized Calls Using JWT Token
# For the kid field in the header, specify your service account's private key ID. You can find this value in the private_key_id field of your service account JSON file.
# For the iss and sub fields, specify your service account's email address. You can find this value in the client_email field of your service account JSON file.
# For the aud field, specify the API endpoint. For example: https://SERVICE.googleapis.com/.
# For the iat field, specify the current Unix time, and for the exp field, specify the time exactly 3600 seconds later, when the JWT will expire.

# All the attributes below are taken from the ke
# {
#   "alg": "RS256",
#   "typ": "JWT",
#   "kid": "private_key_id"
# }
# .
# {
#   "iss": "client_email",
#   "sub": "client_email",
#   "aud": "https://storage.googleapis.com/",
#   "iat": 1511900000,
#   "exp": 1511903600
# }

# Article this code is based on https://developers.google.com/identity/protocols/oauth2
# https://developers.google.com/identity/protocols/oauth2/service-account
# https://developers.google.com/identity/protocols/oauth2/service-account#python_2 

import time 
iat = time.time()
import jwt
import json 

token_file = open('service_accounts_keys.json')
token_data = json.load(token_file)

exp = iat + 3600

payload = {'iss': token_data["client_email"],
           'sub': token_data["client_email"],
           'aud': 'https://storage.googleapis.com/',
           'iat': iat,
           'exp': exp}

additional_headers = {"kid": token_data["private_key_id"]}
signed_jwt = jwt.encode(payload, 
                        token_data["private_key"],
                        headers=additional_headers,
                        algorithm='RS256')
print("\nSignedJWY\n",signed_jwt)

