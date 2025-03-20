import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "767f5d84b3dc4d439e505ec6df3b09d3dbffce69f24d9b4e2eafc44a9f2c4c95")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "7c363fe60a8519be54951c016604dff77ec1a63f4207b843bf8936e20b9eac89")
    # SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sespring2025@localhost:3306/carbon_credit_platform_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = "jwt-secret-key"
    SESSION_TYPE = 'filesystem'
    