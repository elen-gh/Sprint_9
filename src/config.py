import os

class Config:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"
    TIMEOUT = 10
    
    SELENOID_URL = os.getenv("SELENOID_URL", None)
