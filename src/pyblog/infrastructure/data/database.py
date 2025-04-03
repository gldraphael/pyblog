from typing import Optional

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from ..data.base import Base

class AppDb:

    def __init__(self):
        self.__engine: Optional[Engine] = None

    def create_db(self, conn_str, echo=False):
        if self.__engine is not None:
            raise ValueError("create_db() must only be called once.")
        self.__engine = create_engine(conn_str, echo=echo)
        Base.metadata.create_all(self.__engine)
        print(f"Database initialized by {self}")

    def engine(self):
        print(f"Engine accessed by {self}")
        if self.__engine is None:
            raise ValueError("create_db() must be called once before attempting to use the SQL Alchemy Engine")
        return self.__engine

    def session_maker(self):
        return sessionmaker(self.engine())
