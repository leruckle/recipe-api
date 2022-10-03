import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

SQLALCHEMY_DATABASE_URL = "sqlite:///././recipe.db"

engine = sqlalchemy.create_engine(  # type: ignore
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.ext.declarative.declarative_base()


def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
