# backend/app/routers/learnings.py
from fastapi import APIRouter, status
from typing import List
from .. import crud
from ..schemas import LearningCreate

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_learning(payload: LearningCreate):
    doc = await crud.create_learning(payload.dict(exclude_none=True))
    return doc

@router.get("/", response_model=List[dict])
async def get_learnings():
    return await crud.list_learnings()
