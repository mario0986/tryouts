# Tryouts
Tryouts Of Proof of Concepts

## Json Web Token

### References
- https://developers.google.com/identity/protocols/oauth2/service-account#python_2
- https://github.com/jpadilla/pyjwt/
- https://github.com/googleapis/googleapis
- https://jwt.io/#libraries-io


### Outcomes
Generate a token using the `json_web_token.py` based on the `Service Account Key`, once the token was generated I tried to GET the file content from the Cloud Storage.
- Code:     `auth2/json_web_token.py`
- Request: `GET https://storage.googleapis.com/mario-test/mario.json` (On my personal gmail account)
- Response: `AuthenticationRequired`

## Google Auth Library

### References
- https://googleapis.github.io/google-api-python-client/docs/oauth.html 
- https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.service_account.html#google.oauth2.service_account.Credentials
- https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.html

### Outcomes
Generate a signed url with access to the cloud storage
Limitation: Signatures cannot be used to authenticate an upload if the upload uses chunked transfer encoding. Use OAuth 2.0 tokens if you want to use chunked transfer encoding in your uploads.



