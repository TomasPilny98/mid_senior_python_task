from dataclasses import dataclass

from injector import singleton
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session


@singleton
@dataclass
class RepositoryManager:
    engine = create_engine("sqlite:///camera_params.db",
                           pool_recycle=600,
                           connect_args={"check_same_thread": False},
                           echo=False)
    session = scoped_session(sessionmaker(autoflush=True, bind=engine))
    session_scope: Session = session()
    base = declarative_base()
