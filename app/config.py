from pydantic import BaseSettings

class Setting(BaseSettings):
    database_user : str
    database_port : str
    database_name : str
    database_url : str
    database_password : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    class Config:
        env_file = ".env"

setting = Setting()
