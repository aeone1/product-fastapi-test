"""
Create Session
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import Settings

# Create engine only once
engine = create_engine(Settings.db.dsn)

# Create a single session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a scoped session
ScopedSession = scoped_session(SessionLocal)

def session_made():

    """Returns a new session instance."""
    return ScopedSession
