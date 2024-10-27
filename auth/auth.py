from datetime import timedelta
from fastapi import APIRouter
from fastapi import  Depends, HTTPException,status
from sqlalchemy.orm import Session
from config.database import get_db
from config.schema import LoginForm,Token,UserCreate,UserOutput
from config.models import User
from auth import get_password_hash,verify_password,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,get_current_user


router=APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)


@router.post("/register/", response_model=UserOutput, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered.")
    
    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered.")

    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@router.post("/login/", response_model=Token)
def login(form_data: LoginForm, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}






