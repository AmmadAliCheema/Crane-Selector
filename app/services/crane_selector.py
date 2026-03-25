from sqlalchemy.orm import Session, selectinload

from app.models.crane import Crane
from app.schemas.selection import CraneMatch, CraneSelectionResponse


SAFE_RADIUS_NOTE = "Selected using nearest safe radius greater than or equal to requested distance."


def select_crane(db: Session, weight: float, distance: float) -> CraneSelectionResponse:
    cranes = (
        db.query(Crane)
        .options(selectinload(Crane.load_charts))
        .all()
    )

    matches: list[CraneMatch] = []

    for crane in cranes:
        suitable_chart = None

        for chart_row in sorted(crane.load_charts, key=lambda row: row.radius):
            if chart_row.radius >= distance:
                suitable_chart = chart_row
                break

        if not suitable_chart:
            continue

        if suitable_chart.max_load >= weight:
            matches.append(
                CraneMatch(
                    crane_id=crane.id,
                    crane_name=crane.crane_name,
                    crane_model=crane.crane_model,
                    chart_radius_used=suitable_chart.radius,
                    max_load_at_distance=suitable_chart.max_load,
                    notes=SAFE_RADIUS_NOTE,
                )
            )

    matches.sort(key=lambda item: (item.max_load_at_distance, item.chart_radius_used, item.crane_name.lower()))

    if not matches:
        return CraneSelectionResponse(
            success=False,
            required_weight=weight,
            required_distance=distance,
            best_match=None,
            other_matches=[],
            message="No suitable crane found for the given weight and distance.",
        )

    return CraneSelectionResponse(
        success=True,
        required_weight=weight,
        required_distance=distance,
        best_match=matches[0],
        other_matches=matches[1:4],
        message="Suitable crane(s) found successfully.",
    )
