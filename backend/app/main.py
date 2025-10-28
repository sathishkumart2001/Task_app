# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers import tasks, learnings
import logging
from dotenv import load_dotenv
import os

# Load env from file if present (useful for local dev)
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("daily-progress-api")

app = FastAPI(title="Daily Progress API", version="1.0.0")

origins = os.getenv("CORS_ORIGINS", "*").split(",") if os.getenv("CORS_ORIGINS") else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up and initializing DB...")
    await init_db()
    logger.info("DB initialized.")

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
app.include_router(learnings.router, prefix="/api/learnings", tags=["learnings"])

@app.get("/health")
async def health():
    return {"status": "ok"}
