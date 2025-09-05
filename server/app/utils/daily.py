from .helper import get_ist_time
from .celery import celery
from ..models import Lot,User, Notification
from datetime import timedelta
from .email import email_sender
from flask import render_template, current_app
from .. import db

@celery.task
def daily_remainder():
    time_range = get_ist_time() - timedelta(hours=24)
    new_lots = Lot.query.filter(Lot.created_at >= time_range).all()
    for lot in new_lots:
        users = User.query.filter_by(pincode=lot.pincode).all()
        for user in users:
            title = "New Lot in your Area"
            template = render_template("daily_remainder.html", user=user, lot=lot, url=f"{current_app.config['FRONTEND_URL']}/dashboard/available_lots")
            notification = Notification(user_id=user.user_id, title=title, body=template)
            db.session.add(notification)
            db.session.commit()
            email_sender(user.email, title, template, is_html=True)
            
        