"""
Create Session
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Settings


def session():

    Session = sessionmaker(
        bind=create_engine(Settings.db.dsn)
    )

    return Session
