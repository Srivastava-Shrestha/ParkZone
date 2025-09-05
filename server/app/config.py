#ParkZone/server/config.py
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()


class Configuration():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = False
    RAZORPAY_ACCESS_KEY = os.getenv("RAZORPAY_ACCESS_KEY")
    RAZORPAY_CLIENT_ID = os.getenv("RAZORPAY_CLIENT_ID")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_NAME = os.getenv('MAIL_NAME')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    CACHE_TYPE='RedisCache'
    CACHE_REDIS_HOST='localhost'
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_DB=0
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')