from flask_restful import Resource
from flask import request
from ..models import Spot, Reservation, User
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ..utils.helper import role_required, lot_can_delete, get_ist_time
from .. import db


class ReservationApi(Resource):
    
    @jwt_required()
    # @role_required("admin")
    def get(self, spot_id=None):
        try:
            decoded_token = get_jwt()
            role = decoded_token.get("role")
            if not spot_id:
                username = get_jwt_identity()
                user = User.query.filter_by(username=username).first()
                payment_status = request.args.get("payment_status")
                if payment_status=="true":
                    if role == "user":
                        reservations = Reservation.query.filter_by(user_id=user.user_id, payment_status=True).all()
                    else:
                        reservations = Reservation.query.filter_by(payment_status=True).all()
                else:
                    if role == "user":
                        reservations = Reservation.query.filter_by(user_id=user.user_id, payment_status=False).all()
                    else:
                        reservations = Reservation.query.filter_by(payment_status=False).all()
                reservations_detail = [
                    {
                        "reservation_id": reservation.reservation_id,
                        "spot_id": reservation.spot.spot_id,
                        "parking_cost": reservation.parking_cost,
                        "user_id": reservation.user_id,
                        "username":reservation.user.username,
                        "email":reservation.user.email,
                        "vehicle_number": reservation.vehicle_number,
                        "parking_time": reservation.parking_timestamp.strftime('%Y-%m-%d %H:%M:%S') if reservation.parking_timestamp else None,
                        "leaving_time":reservation.leaving_timestamp.strftime('%Y-%m-%d %H:%M:%S') if reservation.leaving_timestamp else None,
                        "prime_location": reservation.spot.lot.prime_location,
                        "address": reservation.spot.lot.address
                    } for reservation in reservations
                ]
                return reservations_detail, 200
            
            spot = Spot.query.filter_by(spot_id=spot_id).first()
            if spot:
                if not spot.status:
                    reservation = spot.reservation[-1]
                    reservation_detail = {
                        "spot_id": spot_id,
                        "status": "Occupied",
                        "user_id": reservation.user_id,
                        "vehicle_number": reservation.vehicle_number,
                        "parking_time": reservation.parking_timestamp.strftime('%Y-%m-%d %H:%M:%S') if reservation.parking_timestamp else None,
                        "current_time": get_ist_time().strftime('%Y-%m-%d %H:%M:%S'),
                        "prime_location": reservation.spot.lot.prime_location,
                        "address": reservation.spot.lot.address
                    }
                    return reservation_detail, 200
                return {"spot_id": spot_id, "status": "Available"}, 200
            return {"message":"Spot not found!"}, 400
        except Exception as e:
            return {"message": f"Something went wrong!{e}"}, 500

        
    @jwt_required()
    @role_required("user")
    def post(self, spot_id):
        try:
            data = request.get_json()
            username = get_jwt_identity()
            user = User.query.filter_by(username=username).first()
            user_id = user.user_id
            vehicle_number = data.get("vehicle_number")
            new_reservation = Reservation(spot_id=spot_id,user_id=user_id,vehicle_number=vehicle_number,payment_status=False) 
            db.session.add(new_reservation)
            spot = Spot.query.get(spot_id)
            spot.status = False
            db.session.commit()
            return {"message": "Spot book successfully!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"Something went wrong!"}, 500
            
    @jwt_required()
    @role_required("user")
    def put(self, reservation_id):
        try:
            data = request.get_json()
            parked = data.get("parked")
            reservation = Reservation.query.get(reservation_id)
            if parked:
                reservation.parking_timestamp = get_ist_time()
            db.session.commit()
            return {"message": "Reservation updated successfully!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": f"Something went wrong!{e}"}, 500