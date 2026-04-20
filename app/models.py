# models for the app
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    location = Column(String)  # "Online" or place
    link = Column(String, nullable=False)
    tags = Column(String)  # comma-separated for now
    trust_level = Column(String, default="manual")
    status = Column(String, default="open")
    
