# backend/app/crud.py
from .database import get_collection
from bson import ObjectId
from typing import List, Dict, Any

TASKS_COLL = "tasks"
LEARNINGS_COLL = "learnings"

async def create_task(task_data: Dict[str, Any]) -> Dict[str, Any]:
    coll = get_collection(TASKS_COLL)
    # ensure default fields
    task_data.setdefault("completed", False)
    res = await coll.insert_one(task_data)
    doc = await coll.find_one({"_id": res.inserted_id})
    return doc

async def list_tasks(limit: int = 200) -> List[Dict[str, Any]]:
    coll = get_collection(TASKS_COLL)
    cursor = coll.find().sort("_id", -1).limit(limit)
    return [doc async for doc in cursor]

async def get_task(task_id: str) -> Dict[str, Any] | None:
    coll = get_collection(TASKS_COLL)
    if not ObjectId.is_valid(task_id):
        return None
    return await coll.find_one({"_id": ObjectId(task_id)})

async def update_task(task_id: str, patch: Dict[str, Any]) -> Dict[str, Any] | None:
    coll = get_collection(TASKS_COLL)
    if not ObjectId.is_valid(task_id):
        return None
    await coll.update_one({"_id": ObjectId(task_id)}, {"$set": patch})
    return await coll.find_one({"_id": ObjectId(task_id)})

async def delete_task(task_id: str) -> bool:
    coll = get_collection(TASKS_COLL)
    if not ObjectId.is_valid(task_id):
        return False
    res = await coll.delete_one({"_id": ObjectId(task_id)})
    return res.deleted_count == 1

# Learnings
async def create_learning(data: Dict[str, Any]) -> Dict[str, Any]:
    coll = get_collection(LEARNINGS_COLL)
    res = await coll.insert_one(data)
    return await coll.find_one({"_id": res.inserted_id})

async def list_learnings(limit: int = 100) -> List[Dict[str, Any]]:
    coll = get_collection(LEARNINGS_COLL)
    cursor = coll.find().sort("_id", -1).limit(limit)
    return [doc async for doc in cursor]
