from app.database import SessionLocal
from app.models import Event
from datetime import datetime

db = SessionLocal()

event = Event(
    title = "Pwndem1c CTF",
    description = "Beginner friendly CTF",
    start_time = datetime(2026, 4, 25, 12, 0),
    location = "Online",
    link = "https://github.com/pwndem1c",
    tags = "CTF, Beginner, Cybersecurity, Online"
)

db.add(event)
db.commit()
db.close()