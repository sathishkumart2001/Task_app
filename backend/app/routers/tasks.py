# backend/app/routers/tasks.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from .. import crud
from ..schemas import TaskCreate, TaskUpdate
from pydantic import BaseModel

router = APIRouter()

class TaskOut(BaseModel):
    # dynamic model for response (to avoid strict schema issues)
    pass

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate):
    doc = await crud.create_task(payload.dict(exclude_none=True))
    return doc

@router.get("/", response_model=List[dict])
async def get_tasks():
    return await crud.list_tasks()

@router.get("/{task_id}")
async def get_task(task_id: str):
    doc = await crud.get_task(task_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Task not found")
    return doc

@router.patch("/{task_id}")
async def patch_task(task_id: str, payload: TaskUpdate):
    updated = await crud.update_task(task_id, payload.dict(exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}")
async def remove_task(task_id: str):
    ok = await crud.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
