from fastapi import FastAPI
from app.database import engine, Base
from app.routes import events
from app.database import SessionLocal
from app.models import Event
from datetime import datetime
from app import models

app = FastAPI() # creates API server
app.include_router(events.router) # include the events router

# Base.metadata.create_all(bind=engine) # creates database tables automatically

db = SessionLocal()
Base.metadata.create_all(bind=engine) # creates database tables automatically

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
