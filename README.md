# Daily Progress App (Flet + FastAPI + MongoDB)

## Overview
A small full-stack Python project:
- Frontend: Flet (Python) — runs in a browser or desktop.
- Backend: FastAPI — REST API serving Tasks & Learnings.
- Database: MongoDB (Atlas recommended).
- Deployment: Render (free tier) using `backend/start.sh` and `backend/render.yaml`.

## Local setup

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp ../.env.example .env
# edit .env and add MONGO_URI
uvicorn app.main:app --reload --port 8000
