from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

#  "<dialect>+<driver>://<username>:<password>@<host>:<port>/<dbname>"
db_url = "sqlite:///database.db"

engine = create_engine(db_url, echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

