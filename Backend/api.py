# API related imports
from fastapi import FastAPI
from pydantic import BaseModel
# Self-made imports
from db import check_password
# Token based imports
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

app = FastAPI()

# ----------- TOKENS -----------

# Declare alg and secret token
with open("SECRET_KEY.txt", "r") as f:
    SECRET_KEY = f.readline()
ALGORITHM = "HS256"
security = HTTPBearer()  # Set up security method

# Function to create a token, with data to encrypt, and an expiry time with a default value of 30 mins
def create_access_token(data: dict, expire_delta: timedelta = timedelta(minutes=30)):
    to_encode = data  # This becomes the payload
    expiry_time = datetime.now(timezone.utc) + expire_delta  # Add the expiry time to the current time to get the expiry time
    to_encode.update({"exp": expiry_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Create the token itself
    return encoded_jwt

# Function to verify a token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  #i.e. The user details
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalud or expired token"
        )
    
# Endpoint to create a protected route. This verifies the token with the user data
@app.get("/api/protected")
def protected_route(user_data: dict = Depends(verify_token)):
    return {"message": f"Welcome {user_data['username']}!"}  # Returns a message based on the payload returned from the verified token

# ----------- API Endpoints -----------

# Create API test call
@app.get("/api/test")
def test_api():
    return {"message": "API is working!"}

# Create a model for the login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Create an endpoint for user login
@app.post("/api/login")
def login(request: LoginRequest):
    # Check with the database if the username and password are correct
    return check_password(request.username, request.password)