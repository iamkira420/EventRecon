# time management
from datetime import datetime

def get_time_status(start_time, end_time=None):
    now = datetime.timezone.utc.now()
    
    if start_time > now:
        delta = start_time - now
        hours = int(delta.total_seconds() // 3600)
        
        if hours < 1:
            return "Starting soon..."
        elif hours < 24:
            return f"Starts in {hours} hours"
        else:
            days = hours // 24
            return f"Starts in {days} days"
        
    if end_time and end_time > now:
        return "Ongoing"
    
    return "Finished"

def time(start_time):
    now = datetime.now()
    delta = start_time - now
    hours = int(delta.total_seconds() // 3600)
    
    if hours < 1:
        return "Starting soon..."
    return f"Starts in {hours} hours"