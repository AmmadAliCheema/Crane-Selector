from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload

from app.db.database import get_db
from app.models.crane import Crane, CraneLoadChart
from app.schemas.crane import (
    CraneCreate,
    CraneDetailResponse,
    CraneResponse,
    CraneUpdate,
    LoadChartCreate,
    LoadChartResponse,
)

router = APIRouter(prefix="/cranes", tags=["Cranes"])


@router.post("", response_model=CraneResponse, status_code=status.HTTP_201_CREATED)
def create_crane(payload: CraneCreate, db: Session = Depends(get_db)):
    crane = Crane(**payload.model_dump())
    db.add(crane)
    db.commit()
    db.refresh(crane)
    return crane


@router.get("", response_model=list[CraneResponse])
def list_cranes(db: Session = Depends(get_db)):
    return db.query(Crane).order_by(Crane.crane_name.asc()).all()


@router.get("/{crane_id}", response_model=CraneDetailResponse)
def get_crane(crane_id: int, db: Session = Depends(get_db)):
    crane = (
        db.query(Crane)
        .options(selectinload(Crane.load_charts))
        .filter(Crane.id == crane_id)
        .first()
    )
    if not crane:
        raise HTTPException(status_code=404, detail="Crane not found.")
    return crane


@router.put("/{crane_id}", response_model=CraneResponse)
def update_crane(crane_id: int, payload: CraneUpdate, db: Session = Depends(get_db)):
    crane = db.query(Crane).filter(Crane.id == crane_id).first()
    if not crane:
        raise HTTPException(status_code=404, detail="Crane not found.")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(crane, field, value)

    db.commit()
    db.refresh(crane)
    return crane


@router.delete("/{crane_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_crane(crane_id: int, db: Session = Depends(get_db)):
    crane = db.query(Crane).filter(Crane.id == crane_id).first()
    if not crane:
        raise HTTPException(status_code=404, detail="Crane not found.")

    db.delete(crane)
    db.commit()
    return None


@router.post("/{crane_id}/load-chart", response_model=LoadChartResponse, status_code=status.HTTP_201_CREATED)
def add_load_chart_row(crane_id: int, payload: LoadChartCreate, db: Session = Depends(get_db)):
    crane = db.query(Crane).filter(Crane.id == crane_id).first()
    if not crane:
        raise HTTPException(status_code=404, detail="Crane not found.")

    existing_row = (
        db.query(CraneLoadChart)
        .filter(CraneLoadChart.crane_id == crane_id, CraneLoadChart.radius == payload.radius)
        .first()
    )
    if existing_row:
        raise HTTPException(
            status_code=400,
            detail="A load chart row already exists for this crane at the same radius.",
        )

    chart_row = CraneLoadChart(crane_id=crane_id, **payload.model_dump())
    db.add(chart_row)
    db.commit()
    db.refresh(chart_row)
    return chart_row


@router.get("/{crane_id}/load-chart", response_model=list[LoadChartResponse])
def list_load_chart_rows(crane_id: int, db: Session = Depends(get_db)):
    crane = db.query(Crane).filter(Crane.id == crane_id).first()
    if not crane:
        raise HTTPException(status_code=404, detail="Crane not found.")

    return (
        db.query(CraneLoadChart)
        .filter(CraneLoadChart.crane_id == crane_id)
        .order_by(CraneLoadChart.radius.asc())
        .all()
    )
