from pydantic import BaseSettings

class Setting(BaseSettings):
    database_user : str
    database_port : str
    database_name : str
    database_url : str
    database_password : str
    
    class Config:
        env_file = ".env"

setting = Setting()
