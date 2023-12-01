from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Postgres
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_HOST: str
    DEBUG: Optional[bool] = False

    # Jwt
    ACCESS_TOKEN_EXPIRES_IN_DAYS: int
    REFRESH_TOKEN_EXPIRES_IN_DAYS: int
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str

    # Pusher
    PUSHER_APP_ID: Optional[str] = None
    PUSHER_KEY: Optional[str] = None
    PUSHER_SECRET: Optional[str] = None
    PUSHER_CLUSTER: Optional[str] = None
    PUSHER_SSL: Optional[bool] = True

    # Channels
    GENERAL_CHANNEL: Optional[str] = "general-channel"
    ALL_CHANNEL: Optional[str] = "all-channel"

    # Cloud
    CLOUD_NAME: str
    API_KEY: str
    API_SECRET: str

    EMAIL: str
    PASSWORD_EMAIL: str

    # VNPAY CONFIG
    VNPAY_RETURN_URL = 'http://localhost:8000/payment_return'  # get from config
    VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
    VNPAY_API_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/api/transaction'
    VNPAY_TMN_CODE = 'RJ9YK2GT'  # Website ID in VNPAY System, get from config
    VNPAY_HASH_SECRET_KEY = 'KQNRPNQNSSUDTSAAIFATZJDDEWVSPMHZ'  # Secret key for create checksum,get from config

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
