from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Issue(BaseModel):
    id: Optional[int]
    text: str
    status: str
    source: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class IssueCreate(BaseModel):
    text: str
    status: str
    source: str


class IssueUpdate(BaseModel):
    text: Optional[str]
    status: Optional[str]
    source: Optional[str]