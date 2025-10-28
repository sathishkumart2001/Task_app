# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to: Optional[str] = None

class LearningCreate(BaseModel):
    title: str
    content: Optional[str] = None
    date: Optional[datetime] = None
