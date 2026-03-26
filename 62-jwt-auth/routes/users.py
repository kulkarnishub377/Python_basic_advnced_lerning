from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import BaseModel

from auth import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
# Note: dependencies must be imported locally to prevent circular imports if using fake_users_db
import dependencies

router = APIRouter()

# --- Mock Database ---
# In a real app this is an actual DB.
fake_users_db = {
    "john@example.com": {
        "username": "john@example.com",
        "full_name": "John Doe",
        # the hashed string of "secret"
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", 
        "is_active": True,
    }
}

class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str

class UserResponse(BaseModel):
    username: str
    full_name: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    """Register a new user and add to mock DB."""
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
        
    hashed_pw = get_password_hash(user.password)
    user_dict = {
        "username": user.username,
        "full_name": user.full_name,
        "hashed_password": hashed_pw,
        "is_active": True
    }
    
    fake_users_db[user.username] = user_dict
    return user_dict


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login endpoint that verifies the password and returns a JWT access token.
    Uses OAuth2PasswordRequestForm (requires x-www-form-urlencoded).
    """
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Generate the JWT encoded string
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: dict = Depends(dependencies.get_current_active_user)):
    """
    A protected route. Only accessible if a valid JWT is passed in the 
    Authorization Header: Bearer <token>.
    """
    return current_user
