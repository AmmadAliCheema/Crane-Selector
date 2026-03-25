from app.db.database import Base, SessionLocal, engine
from app.models.crane import Crane, CraneLoadChart


SAMPLE_CRANES = [
    {
    "crane_name": "Liebherr LTM 1040-2.1",
    "crane_model": "40T Mobile Crane",
    "description": "A compact two-axle crane with high performance and a 35m telescopic boom.",
    "load_charts": [
      {"radius": 2.5, "max_load": 40000},
      {"radius": 5.0, "max_load": 22200},
      {"radius": 10.0, "max_load": 9100},
      {"radius": 15.0, "max_load": 5100},
      {"radius": 20.0, "max_load": 3100},
      {"radius": 31.0, "max_load": 1100}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1055-3.2",
    "crane_model": "55T Mobile Crane",
    "description": "Three-axle all-terrain crane featuring a 40m boom and excellent off-road capability.",
    "load_charts": [
      {"radius": 2.5, "max_load": 55000},
      {"radius": 7.0, "max_load": 18900},
      {"radius": 12.0, "max_load": 9400},
      {"radius": 18.0, "max_load": 5300},
      {"radius": 24.0, "max_load": 3200},
      {"radius": 36.0, "max_load": 1200}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1060-3.1",
    "crane_model": "60T Mobile Crane",
    "description": "Highly maneuverable three-axle crane with a long 48m boom for its class.",
    "load_charts": [
      {"radius": 2.5, "max_load": 60000},
      {"radius": 8.0, "max_load": 19000},
      {"radius": 14.0, "max_load": 9100},
      {"radius": 20.0, "max_load": 5400},
      {"radius": 28.0, "max_load": 3100},
      {"radius": 40.0, "max_load": 1200}
    ]
  },
  {
    "crane_name": "Grove GMK3060L-1",
    "crane_model": "60T Mobile Crane",
    "description": "Known for its extremely strong taxi charts and 48m MEGAFORM boom.",
    "load_charts": [
      {"radius": 3.0, "max_load": 60000},
      {"radius": 10.0, "max_load": 15000},
      {"radius": 16.0, "max_load": 7800},
      {"radius": 22.0, "max_load": 4700},
      {"radius": 30.0, "max_load": 2600},
      {"radius": 44.0, "max_load": 900}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1070-4.2",
    "crane_model": "70T Mobile Crane",
    "description": "Four-axle crane with a 50m boom; a versatile workhorse for mid-size infrastructure.",
    "load_charts": [
      {"radius": 2.5, "max_load": 70000},
      {"radius": 10.0, "max_load": 20500},
      {"radius": 18.0, "max_load": 9500},
      {"radius": 26.0, "max_load": 5100},
      {"radius": 34.0, "max_load": 3200},
      {"radius": 44.0, "max_load": 1800}
    ]
  },
    {
    "crane_name": "Liebherr LTM 1090-4.2",
    "crane_model": "90T Mobile Crane",
    "description": "A powerful 4-axle crane with a 60m main boom and VarioBallast for flexible setup.",
    "load_charts": [
      {"radius": 3.0, "max_load": 90000},
      {"radius": 10.0, "max_load": 29000},
      {"radius": 20.0, "max_load": 10500},
      {"radius": 30.0, "max_load": 5600},
      {"radius": 50.0, "max_load": 1900}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1095-5.1",
    "crane_model": "95T Mobile Crane",
    "description": "A 5-axle all-rounder with a 58m boom, often used for large residential and civil projects.",
    "load_charts": [
      {"radius": 3.0, "max_load": 95000},
      {"radius": 10.0, "max_load": 33500},
      {"radius": 20.0, "max_load": 13300},
      {"radius": 30.0, "max_load": 7300},
      {"radius": 50.0, "max_load": 2200}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1110-5.1",
    "crane_model": "110T Mobile Crane",
    "description": "Features the LICON3 control system and the ability to carry its own counterweight on the road.",
    "load_charts": [
      {"radius": 3.0, "max_load": 110000},
      {"radius": 10.0, "max_load": 37200},
      {"radius": 20.0, "max_load": 16100},
      {"radius": 40.0, "max_load": 5300},
      {"radius": 60.0, "max_load": 1600}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1130-5.1",
    "crane_model": "130T Mobile Crane",
    "description": "A high-capacity 5-axle crane with a 60m boom, offering a balance of mobility and power.",
    "load_charts": [
      {"radius": 3.0, "max_load": 130000},
      {"radius": 10.0, "max_load": 43500},
      {"radius": 20.0, "max_load": 19100},
      {"radius": 40.0, "max_load": 6500},
      {"radius": 70.0, "max_load": 900}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1150-5.3",
    "crane_model": "150T Mobile Crane",
    "description": "The 'Jewel' of the fleet with a 66m boom and class-leading taxi load charts.",
    "load_charts": [
      {"radius": 3.0, "max_load": 150000},
      {"radius": 10.0, "max_load": 47200},
      {"radius": 20.0, "max_load": 19500},
      {"radius": 40.0, "max_load": 6600},
      {"radius": 70.0, "max_load": 1100}
    ]
  },
  {
    "crane_name": "Grove GMK5150XL",
    "crane_model": "150T Mobile Crane",
    "description": "Features an extraordinary 68.7m main boom, one of the longest in the 150-tonne class.",
    "load_charts": [
      {"radius": 3.0, "max_load": 150000},
      {"radius": 12.0, "max_load": 36500},
      {"radius": 24.0, "max_load": 15200},
      {"radius": 40.0, "max_load": 7300},
      {"radius": 80.0, "max_load": 1100}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1160-5.2",
    "crane_model": "180T Mobile Crane",
    "description": "Efficient 5-axle crane with a 62m boom, utilizing ECOmode to reduce fuel and noise.",
    "load_charts": [
      {"radius": 3.0, "max_load": 180000},
      {"radius": 10.0, "max_load": 56000},
      {"radius": 20.0, "max_load": 27200},
      {"radius": 40.0, "max_load": 9800},
      {"radius": 70.0, "max_load": 2200}
    ]
  },
  {
    "crane_name": "Grove GMK5250XL-1",
    "crane_model": "250T Mobile Crane",
    "description": "Southern's long-reach specialist with a massive 78.5m main boom.",
    "load_charts": [
      {"radius": 3.0, "max_load": 250000},
      {"radius": 10.0, "max_load": 72000},
      {"radius": 30.0, "max_load": 16500},
      {"radius": 50.0, "max_load": 7600},
      {"radius": 70.0, "max_load": 2000}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1300-6.3",
    "crane_model": "300T Mobile Crane",
    "description": "A 6-axle giant with a 90m main boom, designed for massive reach without jibs.",
    "load_charts": [
      {"radius": 3.0, "max_load": 300000},
      {"radius": 10.0, "max_load": 85000},
      {"radius": 30.0, "max_load": 23000},
      {"radius": 60.0, "max_load": 6500},
      {"radius": 90.0, "max_load": 1200}
    ]
  },
  {
    "crane_name": "Liebherr LTM 1450-8.1",
    "crane_model": "450T Mobile Crane",
    "description": "The flagship 8-axle crane. Can perform jobs usually reserved for the 500T class.",
    "load_charts": [
      {"radius": 3.0, "max_load": 450000},
      {"radius": 10.0, "max_load": 140000},
      {"radius": 30.0, "max_load": 48000},
      {"radius": 60.0, "max_load": 12500},
      {"radius": 100.0, "max_load": 1800}
    ]
  },
    {
    "crane_name": "Kato CR-200Ri",
    "crane_model": "20T City Crane",
    "description": "Compact 2-axle city crane with a 28m boom and 5.8m hydraulic jib. Ideal for tight urban alleys.",
    "load_charts": [
      {"radius": 2.5, "max_load": 20000},
      {"radius": 8.0, "max_load": 5000},
      {"radius": 14.0, "max_load": 1850},
      {"radius": 20.0, "max_load": 800},
      {"radius": 24.0, "max_load": 450}
    ]
  },
  {
    "crane_name": "Kato CR-250Rv",
    "crane_model": "25T City Crane",
    "description": "The latest generation Kato with a 29m main boom and improved safety features for street works.",
    "load_charts": [
      {"radius": 3.0, "max_load": 25000},
      {"radius": 10.0, "max_load": 5000},
      {"radius": 18.0, "max_load": 1750},
      {"radius": 24.0, "max_load": 850},
      {"radius": 28.0, "max_load": 500}
    ]
  },
  {
    "crane_name": "Liebherr LTC 1050-3.1",
    "crane_model": "50T Compact Crane",
    "description": "Features a 'telescoping' operator cab that can be raised for better visibility. Designed for indoor/low-headroom industrial lifts.",
    "load_charts": [
      {"radius": 3.0, "max_load": 50000},
      {"radius": 10.0, "max_load": 10800},
      {"radius": 20.0, "max_load": 3800},
      {"radius": 30.0, "max_load": 1600},
      {"radius": 34.0, "max_load": 1100}
    ]
  },
  {
    "crane_name": "Spierings SK597-AT4 eLift",
    "crane_model": "Mobile Tower Crane (Hybrid)",
    "description": "A 4-axle mobile tower crane that can operate 100% electrically. Combines the mobility of a truck with the reach of a tower crane.",
    "load_charts": [
      {"radius": 3.5, "max_load": 7000},
      {"radius": 14.0, "max_load": 7000},
      {"radius": 28.0, "max_load": 3350},
      {"radius": 40.0, "max_load": 2150},
      {"radius": 48.0, "max_load": 1700}
    ]
  },
  {
    "crane_name": "Liebherr MK 140-5.1",
    "crane_model": "Mobile Tower Crane",
    "description": "Flagship 5-axle mobile tower crane. Features a 60m jib and 'luffing' mode for working over tall buildings.",
    "load_charts": [
      {"radius": 3.5, "max_load": 8000},
      {"radius": 15.0, "max_load": 8000},
      {"radius": 30.0, "max_load": 3850},
      {"radius": 45.0, "max_load": 2350},
      {"radius": 60.0, "max_load": 1900}
    ]
  }
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        if db.query(Crane).first():
            print("Database already has crane data. Skipping seed.")
            return

        for crane_data in SAMPLE_CRANES:
            load_charts = crane_data.pop("load_charts")
            crane = Crane(**crane_data)
            db.add(crane)
            db.flush()

            for row in load_charts:
                db.add(CraneLoadChart(crane_id=crane.id, **row))

        db.commit()
        print("Sample crane data inserted successfully.")
    except Exception as exc:
        db.rollback()
        print(f"Seed failed: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
