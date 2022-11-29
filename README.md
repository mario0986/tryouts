# Tryouts
Tryouts Of Proof of Concepts

## Json Web Token

### Instalation
- `pip install PyJWT`

### Reference
- https://developers.google.com/identity/protocols/oauth2/service-account#python_2
- https://github.com/jpadilla/pyjwt/
- https://github.com/googleapis/googleapis
- https://jwt.io/#libraries-io


### Outcomes
Generate a token using the `json_web_token.py` based on the `Service Account Key`, once the token was generated I tried to GET the file content from the Cloud Storage.
- Code:     `auth2/json_web_token.py`
- Request: `GET https://storage.googleapis.com/mario-test/mario.json` (On my personal gmail account)
- Response: `AuthenticationRequired`




