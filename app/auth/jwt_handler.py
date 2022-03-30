# Script responsible for handling JWT tokens, 
# encoding and decoding them

import time
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')


# Function returns the generated tokens
def token_response(token: str):
    """
    Return a token response
    """
    return {
        'access token': token
    }

# Function used to sign JWT token and set its expiration time
def signJWT(userID: str):
    """
    Sign a JWT token
    """
    payload = {
        'userID': userID,
        'exp': int(time.time()) + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)

def decode_JWT(token: str):
    """
    Decode a JWT token
    """
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except jwt.ExpiredSignatureError:
        return 'Token expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'