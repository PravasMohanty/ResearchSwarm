import os
import json
from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials
)

from pydantic import BaseModel

from config.settings import settings

from services.research import run_research


# Absolute path to backend/results/ regardless of CWD
RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")

router = APIRouter()

security = HTTPBasic()


class LoginRequest(BaseModel):
    username: str
    password: str


class ResearchRequest(BaseModel):
    query: str


def authenticate(
    credentials: HTTPBasicCredentials = Depends(security)
):

    if (
        credentials.username != settings.APP_USERNAME
        or credentials.password != settings.APP_PASSWORD
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return credentials.username


@router.post("/auth/login")
async def login(request: LoginRequest):
    """
    Simple credential check for the frontend.
    Returns a success message and the username so the frontend
    can store it for subsequent HTTP-Basic authenticated requests.
    """
    if (
        request.username != settings.APP_USERNAME
        or request.password != settings.APP_PASSWORD
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "status": "ok",
        "username": request.username,
        "message": "Login successful"
    }


@router.post("/research/start")
async def start_research(
    request: ResearchRequest,
    user: str = Depends(authenticate)
):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    result = await run_research(request.query)
    return result


# ───────── History endpoints ─────────


@router.get("/research/history")
async def list_history(
    user: str = Depends(authenticate)
):
    """
    Return a list of all past research results (newest first).
    Each entry contains: filename, query, created_at.
    """
    os.makedirs(RESULTS_DIR, exist_ok=True)

    entries = []
    for fname in os.listdir(RESULTS_DIR):
        if not fname.endswith(".json"):
            continue

        filepath = os.path.join(RESULTS_DIR, fname)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            entries.append({
                "filename": fname,
                "query": data.get("query", "Unknown"),
                "title": data.get("raw_report", {}).get("title", "Untitled"),
                "created_at": data.get("created_at", ""),
            })
        except (json.JSONDecodeError, OSError):
            continue

    # Sort newest first
    entries.sort(key=lambda e: e["created_at"], reverse=True)

    return {"history": entries}


@router.get("/research/history/{filename}")
async def get_history_entry(
    filename: str,
    user: str = Depends(authenticate)
):
    """
    Return the full contents of a specific history file.
    """
    # Prevent path traversal
    if ".." in filename or "/" in filename or "\\" in filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    filepath = os.path.join(RESULTS_DIR, filename)

    if not os.path.isfile(filepath):
        raise HTTPException(status_code=404, detail="Report not found")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        raise HTTPException(status_code=500, detail="Failed to read report")

    return data