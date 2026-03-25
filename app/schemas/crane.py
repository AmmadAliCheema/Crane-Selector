from typing import Optional

from pydantic import BaseModel, Field


class CraneBase(BaseModel):
    crane_name: str = Field(..., min_length=2, max_length=255)
    crane_model: str = Field(..., min_length=2, max_length=255)
    description: Optional[str] = Field(default=None, max_length=500)


class CraneCreate(CraneBase):
    pass


class CraneUpdate(BaseModel):
    crane_name: Optional[str] = Field(default=None, min_length=2, max_length=255)
    crane_model: Optional[str] = Field(default=None, min_length=2, max_length=255)
    description: Optional[str] = Field(default=None, max_length=500)


class LoadChartBase(BaseModel):
    radius: float = Field(..., gt=0, description="Working radius / distance in meters")
    max_load: float = Field(..., gt=0, description="Maximum safe load in kg")


class LoadChartCreate(LoadChartBase):
    pass


class LoadChartResponse(LoadChartBase):
    id: int
    crane_id: int

    model_config = {"from_attributes": True}


class CraneResponse(CraneBase):
    id: int

    model_config = {"from_attributes": True}


class CraneDetailResponse(CraneResponse):
    load_charts: list[LoadChartResponse] = []

    model_config = {"from_attributes": True}
