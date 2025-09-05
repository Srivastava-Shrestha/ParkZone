from ..models import Reservation
from .celery import celery
import csv
import io
from flask import render_template
from .email import csv_email_sender

@celery.task
def export_user_usage_csv(user_id,email):
    output = io.StringIO()
    headers = ["reservation_id","lot_id", "spot_id", "prime_location", "parking_cost", "parking_timestamp"]
    csv_writer = csv.DictWriter(output, fieldnames=headers)
    csv_writer.writeheader()
    reservations = Reservation.query.filter_by(user_id=user_id).all()
    for reservation in reservations:
        csv_writer.writerow({
            "reservation_id": reservation.reservation_id,
            "lot_id": reservation.spot.lot.lot_id,
            "spot_id": reservation.spot.spot_id,
            "prime_location": reservation.spot.lot.prime_location,
            "parking_cost": reservation.parking_cost,
            "parking_timestamp":reservation.parking_timestamp
        })
            
    csv_file = output.getvalue()
    output.close()
    body = render_template("csv_export.html")
    csv_email_sender(email,"Your CSV is ready!",body,csv_file)
    
    
    