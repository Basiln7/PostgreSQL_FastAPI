import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        from_attributes = True


settings = Settings()

# Debugging (optional)
print(f"📡 Loaded DB URL: {settings.DATABASE_URL}")
