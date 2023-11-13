from sqlalchemy import create_engine, Table, insert
from sqlalchemy.orm import Session, registry

from host import Host


class Database:
    def __init__(self, url: str, table_name: str) -> None:
        self.engine = create_engine(url=url, pool_pre_ping=True)
        self.session = Session(bind=self.engine)
        self.mapper_registry = registry()
        self.table = Table(
            table_name,
            self.mapper_registry.metadata,
            autoload_with=self.engine
        )

    def save_profile(self, host: Host, columns_map: dict[str, str]) -> None:
        params = {}
        for col, attr in columns_map.items():
            params[col] = getattr(host, attr)
            
        self.session.execute(insert(self.table).values(params))
        self.session.commit()

    def __del__(self):
        self.session.close()
