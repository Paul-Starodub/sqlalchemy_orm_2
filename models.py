from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

#  "<dialect>+<driver>://<username>:<password>@<host>:<port>/<dbname>"
db_url = "sqlite:///database.db"

engine = create_engine(db_url, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self) -> str:
        return f"<User(name={self.name}, age={self.age})>"


Base.metadata.create_all(engine)
