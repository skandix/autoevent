import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.API_HOST = os.environ.get("API_HOST")
        self.API_PORT = os.environ.get("API_PORT")
        self.API_DEBUG = os.environ.get("API_DEBUG")
        self.API_RELOAD = os.environ.get("API_RELOAD")