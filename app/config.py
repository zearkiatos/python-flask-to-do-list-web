import os

class Config:
    SECRET_KEY = os.environ.get('SUPER_SECRET')