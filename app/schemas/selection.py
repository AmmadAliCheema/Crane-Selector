from typing import Optional

from pydantic import BaseModel, Field


class CraneSelectionRequest(BaseModel):
    weight: float = Field(..., gt=0, description="Required load weight in kg")
    distance: float = Field(..., gt=0, description="Required working distance in meters")


class CraneMatch(BaseModel):
    crane_id: int
    crane_name: str
    crane_model: str
    chart_radius_used: float
    max_load_at_distance: float
    notes: str


class CraneSelectionResponse(BaseModel):
    success: bool
    required_weight: float
    required_distance: float
    best_match: Optional[CraneMatch] = None
    other_matches: list[CraneMatch] = Field(default_factory=list,max_length=3)
    message: str
