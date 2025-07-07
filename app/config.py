import os

class Config:
    AZURE_API_KEY = os.getenv("AZURE_API_KEY")
    AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
    API_VERSION = os.getenv("API_VERSION")
