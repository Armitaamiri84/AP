import sys

def time_to_minutes(time):
    hour,minute = time.split(':')
    return int(hour)*60 + int(minute)


