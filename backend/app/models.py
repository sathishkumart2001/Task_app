# backend/app/models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

# Helper for ObjectId in Pydantic models
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to: Optional[str] = None

class TaskInDB(TaskBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    completed: bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        schema_extra = {"example": {"title": "Daily standup", "description": "Prepare update"}}


class LearningBase(BaseModel):
    title: str
    content: Optional[str] = None
    date: Optional[datetime] = None

class LearningCreate(LearningBase):
    pass

class LearningInDB(LearningBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
