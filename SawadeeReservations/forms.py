from datetime import time, datetime


# Define available time slots
TIME_SLOTS = [
    (time(hour, 0), f"{hour:02}:00 - {hour + 2:02}:00")
    for hour in range(10, 22, 2)
]

# Define available guest options
GUEST_OPTIONS = [(i, i) for i in range(4, 21)]  # Options from 4 to 20

