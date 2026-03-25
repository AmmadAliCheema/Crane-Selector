# Crane Selector Backend

FastAPI backend for a crane selection system. The frontend can be built separately in WordPress and call this API.

## What it does
- Accepts **weight** and **distance** from the user
- Checks crane load chart data stored in the database
- Returns the **best suitable crane** and all other suitable cranes
- Lets admin users manage cranes and load charts through API endpoints

## Project structure

```text
crane_backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── scripts/
│   └── seed_data.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn app.main:app --reload
```

Open:
- API docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## Seed sample data

```bash
python scripts/seed_data.py
```

## Main endpoint for WordPress

### POST `/api/v1/select-crane`

Request body:

```json
{
  "weight": 4500,
  "distance": 15
}
```

Response:

```json
{
  "success": true,
  "required_weight": 4500,
  "required_distance": 15,
  "best_match": {
    "crane_id": 1,
    "crane_name": "Liebherr LTM 1050",
    "crane_model": "50T Mobile Crane",
    "chart_radius_used": 15,
    "max_load_at_distance": 5000,
    "notes": "Selected using nearest safe radius greater than or equal to requested distance."
  },
  "other_matches": [
    {
      "crane_id": 2,
      "crane_name": "Tadano AC 60",
      "crane_model": "60T Mobile Crane",
      "chart_radius_used": 15,
      "max_load_at_distance": 6500,
      "notes": "Selected using nearest safe radius greater than or equal to requested distance."
    }
  ],
  "message": "Suitable crane(s) found successfully."
}
```

## Notes
- The selector uses the **nearest safe greater-or-equal radius**.
- Example: if user enters `13m`, and chart has `12m` and `14m`, the system uses `14m`.
- This is safer than using a smaller radius.

## Suggested WordPress integration
- Build a form in WordPress with:
  - weight
  - distance
- Submit to `POST /api/v1/select-crane`
- Show returned crane details on the frontend

## Important
This is a **selection support tool**. In a real crane business, final lifting decisions should still be checked by qualified personnel using official crane charts and site conditions.
