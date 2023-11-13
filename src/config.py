import yaml
from pydantic_settings import BaseSettings


class Profiles(BaseSettings):
    path: str


class Ssh(BaseSettings):
    commands: dict[str, str]


class Db(BaseSettings):
    url: str
    table: str
    columns: dict[str, str]


class Config(BaseSettings):
    profiles: Profiles
    ssh: Ssh
    logger: dict
    db: Db

    @staticmethod
    def load(path: str) -> 'Config':
        with open(path) as f:
            yaml_cfg = yaml.safe_load(f)
        return Config(**yaml_cfg)
