from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Event
from datetime import datetime, timedelta
from app.utils.time import get_time_status
print("EVENT MODULES LOADED SUCCESSFULLY")

router = APIRouter(prefix="/events", tags=["Events"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# GET all events
@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

    result = []
    for event in events:
        result.append({
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "start_time": event.start_time,
            "status": get_time_status(event.start_time, event.end_time),
            "location": event.location,
            "link": event.link,
            "tags": event.tags,
            "time_status": get_time_status(event.start_time)
        })
    return result

# GET weekend events
@router.get("/weekend")
def get_weekend_events(db: Session = Depends(get_db)):
    now = datetime.now()
    weekend = now + timedelta(days = 3)
    return db.query(Event).filter(Event.start_time <= weekend).all()

