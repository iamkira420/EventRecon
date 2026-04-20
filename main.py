from fastapi import FastAPI, HTTPException

app = FastAPI()


events = []

@app.get("/")
def root():
    return {"message": "What’s actually worth my time this weekend nearby?"}

@app.post("/events")
def create_event(event: str):
    events.append(event)
    return events

@app.get("/events/{event_id}")
def get_event(event_id: int) -> str:
    if event_id < len(events):
        return events[event_id]
    else:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")