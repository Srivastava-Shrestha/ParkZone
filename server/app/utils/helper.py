#ParkZone/server/app/utils.py

from flask_jwt_extended import get_jwt
import re
from datetime import datetime
import pytz


def check_email_format(email):
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_pattern, email) is not None

def check_username_format(username):
    regex_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(regex_pattern, username) is not None

def role_required(role):  
    def wrapper(fn):    
        def extra_checks(*args, **kwargs):   
            decoded_data = get_jwt()   
            if decoded_data.get('role') != role:
                return {'message': 'Forbidden, access denied!'}, 403
            granted = fn(*args, **kwargs)
            return granted
        return extra_checks
    return wrapper

def lot_can_delete(lot):
    for spot in lot.spots:
        if spot.status is False:  
            return False
    return True


def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist) 

def get_past_months(k=3):
    now = datetime.now()
    months = []
    for i in range(k):
        month = (now.month - i - 1) % 12 + 1
        year = now.year - ((now.month - i - 1) // 12)
        months.append((year, month))
    return months[::-1]