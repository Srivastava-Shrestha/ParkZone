from .helper import get_ist_time
from .celery import celery
from ..models import Lot,User, Notification, Reservation
from datetime import timedelta
from .email import email_sender
from flask import render_template, current_app
from .. import db
import calendar

@celery.task
def monthly_remainder():
    time_range = get_ist_time().replace(tzinfo=None) - timedelta(days=30)
    month_name = calendar.month_name[time_range.month]
    users = User.query.all()
    title = "Monthly report - ParkZone"
    for user in users:
        user_reservations = user.reservations
        reservation_list = []
        lot_counts = {}
        monthly_cost = 0
        for reservation in user_reservations:
            if reservation.parking_timestamp and reservation.parking_timestamp >= time_range:
                reservation_list.append(reservation)
                monthly_cost += reservation.parking_cost or 0
                lot = reservation.spot.lot.prime_location
                if lot in lot_counts:
                    lot_counts[lot] += 1
                else:
                    lot_counts[lot] = 1
        most_visited_lot = max(lot_counts, key=lot_counts.get) if lot_counts else None
        total_reservation = len(reservation_list)
        template = render_template("monthly_report.html",user=user,report_month=month_name, monthly_cost=monthly_cost, most_visited_lot=most_visited_lot,total_reservation=total_reservation)
        email_sender(user.email, title, template, is_html=True)
        
        