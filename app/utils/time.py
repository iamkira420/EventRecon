# time management
from datetime import datetime

def time(start_time):
    now = datetime.now()
    delta = start_time - now
    hours = int(delta.total_seconds() // 3600)
    
    if hours < 1:
        return "Starting soon..."
    return f"Starts in {hours} hours"