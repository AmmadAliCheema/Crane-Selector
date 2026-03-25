from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.selection import CraneSelectionRequest, CraneSelectionResponse
from app.services.crane_selector import select_crane

router = APIRouter(tags=["Crane Selection"])


@router.post("/select-crane", response_model=CraneSelectionResponse)
def choose_crane(payload: CraneSelectionRequest, db: Session = Depends(get_db)):
    return select_crane(db=db, weight=payload.weight, distance=payload.distance)
