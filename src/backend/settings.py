from pydantic_settings import BaseSettings


class Settings(BaseSettings):


    version_api: str = "/v1/"