#!/usr/bin/env bash
# backend/start.sh
set -e

# If .env exists, export vars for the process
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Default port
PORT=${PORT:-8000}

exec gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:${PORT} --workers 1 --log-level info
