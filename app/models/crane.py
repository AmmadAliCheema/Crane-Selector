from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.db.database import Base


class Crane(Base):
    __tablename__ = "cranes"

    id = Column(Integer, primary_key=True, index=True)
    crane_name = Column(String(255), nullable=False)
    crane_model = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    load_charts = relationship(
        "CraneLoadChart",
        back_populates="crane",
        cascade="all, delete-orphan",
        order_by="CraneLoadChart.radius",
    )


class CraneLoadChart(Base):
    __tablename__ = "crane_load_charts"

    id = Column(Integer, primary_key=True, index=True)
    crane_id = Column(Integer, ForeignKey("cranes.id", ondelete="CASCADE"), nullable=False)
    radius = Column(Float, nullable=False)
    max_load = Column(Float, nullable=False)

    crane = relationship("Crane", back_populates="load_charts")
