# FastAPI-Authentication-with-JWT
This tutorial will teach you how to create authentication in a FastAPI application using JSON Web Tokens.

[Medium Article](https://medium.com/@kshitij.zutshi/fast-api-authentication-with-jwt-c39194155a57) 🚀


### API with JWT Auth Demo

[![Fast API Authentication with JWT](https://res.cloudinary.com/marcomontalbano/image/upload/v1648614123/video_to_markdown/images/youtube--c91Fv2ZTEfs-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=c91Fv2ZTEfs "Fast API Authentication with JWT")

### Steps and File description

I will be building a secured mini-blog CRUD app for creating and reading blog posts.

Before we proceed, let's define a pydantic model for the posts.

#### Model File

In model.py:

* Define the Schemas for Post creation, User login, sign up etc
* Config of schema also added for each schema function

#### JWT Authentication

In this section, we'll create a JWT token handler and a class to handle bearer tokens.

Before beginning, install PyJWT, for encoding and decoding JWTs. We'll also be using and python-decouple for reading environment variables.

#### JWT Handler

The JWT handler will be responsible for signing, encoding, decoding, and returning JWT tokens. In the code, we imported the time, typing, jwt, and decouple modules. The time module is responsible for setting an expiry for the tokens. Every JWT has an expiry date and/or time where it becomes invalid. The jwt module is responsible for encoding and decoding generated token strings. Lastly, the token_response function is a helper function for returning generated tokens.

#### JWT Secret and Algorithm

Next, create an environment file called .env in the base directory:
```
secret=please_please_update_me_please
algorithm=HS256
```
The secret key is used for encoding and decoding JWT strings.

The algorithm value on the other hand is the type of algorithm used in the encoding process.

In the **signJWT** function, we defined the payload, a dictionary containing the user_id passed into the function, and an expiry time of ten minutes from when it is generated. Next, we created a token string comprising of the payload, the secret, and the algorithm type and then returned it.

The **decodeJWT** function takes the token and decodes it with the aid of the jwt module and then stores it in a decoded_token variable. Next, we returned decoded_token if the expiry time is valid, otherwise, we returned None.

#### User Registration and Login

Moving along, let's wire up the routes, schemas, and helpers for handling user registration and login.

#### Securing Routes

With the authentication in place, let's secure the create route.

#### JWT Bearer

Now we need to verify the protected route, by checking whether the request is authorized or not. This is done by scanning the request for the JWT in the Authorization header. FastAPI provides the basic validation via the HTTPBearer class. We can use this class to extract and parse the token. Then, we'll verify it using the decodeJWT function defined in app/auth/auth_handler.py.

Create a new file in the "auth" folder called auth_bearer.py

So, the JWTBearer class is a subclass of FastAPI's HTTPBearer class that will be used to persist authentication on our routes.

Init

In the __init__ method, we enabled automatic error reporting by setting the boolean auto_error to True.

Call

In the __call__ method, we defined a variable called credentials of type HTTPAuthorizationCredentials, which is created when the JWTBearer class is invoked. We then proceeded to check if the credentials passed in during the course of invoking the class are valid:

    If the credential scheme isn't a bearer scheme, we raised an exception for an invalid token scheme.
    If a bearer token was passed, we verified that the JWT is valid.
    If no credentials were received, we raised an invalid authorization error.

Verify

The verify_jwt method verifies whether a token is valid. The method takes a jwtoken string which it then passes to the decodeJWT function and returns a boolean value based on the outcome from decodeJWT.

#### Dependency Injection

To secure the routes, we'll leverage dependency injection via FastAPI's Depends.

Start by updating the imports by adding the JWTBearer class as well as Depends

In the POST route, add the dependencies argument to the @app property

#### Conclusion

This tutorial covered the process of securing a FastAPI application with JSON Web Tokens. Thanks for reading.

Future challenges:

    * Hash the passwords before saving them using [bcrypt](https://github.com/pyca/bcrypt/) or [passlib](https://passlib.readthedocs.io/).
    * Move the users and posts from temporary storage to a database like MongoDB or Postgres. You can follow the steps in [Building a CRUD App with FastAPI and MongoDB](https://testdriven.io/blog/fastapi-mongo/) to set up a MongoDB database and deploy to Heroku.
    * Add refresh tokens to automatically issue new JWTs when they expire. Don't know where to start? Check out [this](https://stackoverflow.com/questions/46197050/flask-jwt-extend-validity-of-token-on-each-request/46284627#46284627) explanation by the author of Flask-JWT.
    * Add routes for updating and deleting posts.


### References

https://video-to-markdown.marcomontalbano.com/

https://github.com/BekBrace/FASTAPI-and-JWT-Authentication

https://www.youtube.com/watch?v=0_seNFCtglk&ab_channel=BekBrace

https://github.com/testdrivenio/fastapi-jwt
