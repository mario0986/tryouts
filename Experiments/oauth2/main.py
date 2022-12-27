import time
import json
import jwt
import requests
import httplib2

# Project ID for this request.
project = 'programiv'

# The name of the zone for this request.
zone = 'us-east1'

# Service Account Credentials, Json format
json_filename = 'service_accounts_keys.json'

# Permissions to request for Access Token
scopes = "https://www.googleapis.com/auth/devstorage.read_write"

# Set how long this token will be valid in seconds
expires_in = 3600	# Expires in 1 hour

def load_json_credentials(filename):
    ''' Load the Google Service Account Credentials from Json file '''

    with open(filename, 'r') as f:
        data = f.read()

    return json.loads(data)

def load_private_key(json_cred):
    ''' Return the private key from the json credentials '''

    return json_cred['private_key']

def create_signed_jwt(pkey, pkey_id, email, scope):
    '''
    Create a Signed JWT from a service account Json credentials file
    This Signed JWT will later be exchanged for an Access Token
    '''

    # Google Endpoint for creating OAuth 2.0 Access Tokens from Signed-JWT
    auth_url = "https://www.googleapis.com/oauth2/v4/token"

    issued = int(time.time())
    expires = issued + expires_in	# expires_in is in seconds

    # Note: this token expires and cannot be refreshed. The token must be recreated

    # JWT Headers
    additional_headers = {
            'kid': pkey_id,
            "alg": "RS256", # Google uses SHA256withRSA
            "typ": "JWT"
    }

    # JWT Payload
    payload = {
        "iss": email,		# Issuer claim
        "sub": email,		# Issuer claim
        "aud": auth_url,	# Audience claim
        "iat": issued,		# Issued At claim
        "exp": expires,		# Expire time
        "scope": scope		# Permissions
    }

    # Encode the headers and payload and sign creating a Signed JWT (JWS)
    sig = jwt.encode(payload, pkey, algorithm="RS256", headers=additional_headers)

    return sig

# This will happen on SAP
def exchangeJwtForAccessToken(signed_jwt):
    '''
    This function takes a Signed JWT and exchanges it for a Google OAuth Access Token
    '''

    auth_url = "https://www.googleapis.com/oauth2/v4/token"

    params = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": signed_jwt
    }    

    r = requests.post(auth_url, data=params)
    
    if r.ok:
        return(r.json()['access_token'], '')

    return None, r.text
    '''
    This functions lists the Google Compute Engine Instances in one zone
    '''

    # Endpoint that we will call
    url = "https://www.googleapis.com/compute/v1/projects/" + project + "/zones/" + zone + "/instances"

    # One of the headers is "Authorization: Bearer $TOKEN"
    headers = {
        "Host": "www.googleapis.com",
        "Authorization": "Bearer " + accessToken,
        "Content-Type": "application/json"
    }

    h = httplib2.Http()

    resp, content = h.request(uri=url, method="GET", headers=headers)

    status = int(resp.status)

    if status < 200 or status >= 300:
        print('Error: HTTP Request failed')
        return

    j = json.loads(content.decode('utf-8').replace('\n', ''))

    print('Compute instances in zone', zone)
    print('------------------------------------------------------------')
    for item in j['items']:
        print(item['name'])

if __name__ == '__main__':
    cred = load_json_credentials(json_filename)
    
    private_key = load_private_key(cred)
    
    s_jwt = create_signed_jwt(
            private_key,
            cred['private_key_id'],
            cred['client_email'],
            scopes)

    token, err = exchangeJwtForAccessToken(s_jwt)
    print(token)

    if token is None:
        print('Error:', err)
        exit(1)
