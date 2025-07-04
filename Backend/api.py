from fastapi import FastAPI
from pydantic import BaseModel
from db import check_password

app = FastAPI()

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