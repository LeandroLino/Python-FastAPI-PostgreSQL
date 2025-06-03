from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class APICounter(Base):
    __tablename__ = "api_counters"
    
    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, unique=True, index=True)
    count = Column(Integer, default=0)
