import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "gizli-anahtar-buraya")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///leads.db"
    )
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    BUSINESS_CONTEXT = os.environ.get("BUSINESS_CONTEXT")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")