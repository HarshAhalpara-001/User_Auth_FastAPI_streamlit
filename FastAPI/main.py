from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

SECRET_KEY = "H@rshahalpara001"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})  # Add expiration to the token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

app = FastAPI()

users_db = {} # temp db for demo

class User(BaseModel):
    username : str
    password : str

@app.post('/register')
async def register(user : User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail = 'User already registered')
    users_db[user.username] = hash_password(user.password)
    print(users_db)
    return {'succes'}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

class Token(BaseModel):
    access_token: str
    token_type: str

@app.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(form_data.password, users_db[form_data.username]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get('/')
async def check():
    return {'Running': 'Yes All OK!'}