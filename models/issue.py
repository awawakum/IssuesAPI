from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from database import Base


class IssueModel(Base):
    """Issue ORM model"""
    __tablename__ = "issues"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(128), nullable=False)
    status = Column(String(50), nullable=False)
    source = Column(String(50), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())