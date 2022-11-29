# tryouts
Tryouts Of Proof of Concepts

## Json Web Token

### Instalation
- `pip install PyJWT`

### Outcomes
Generate a token using the `json_web_token.py` based on the `Service Account Key`, once the token was generated I tried to GET the file content from the Cloud Storage.
- Code:     `auth2/json_web_token.py`
- Request: `GET https://storage.googleapis.com/mario-test/mario.json` (On my personal gmail account)
- Response: `AuthenticationRequired`




