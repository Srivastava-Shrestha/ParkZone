
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request, current_app
import razorpay
from ..models import Reservation
from ..utils.helper import get_ist_time, role_required
from .. import db


class PaymentApi(Resource):
    def get(self):
        razorpay_client = razorpay.Client(auth=(current_app.config["RAZORPAY_CLIENT_ID"],current_app.config["RAZORPAY_ACCESS_KEY"]))
        reservation_id = request.args.get("reservation_id", type=int)
        if reservation_id:
            reservation = Reservation.query.get_or_404(reservation_id) 
            parking_time = reservation.parking_timestamp
            leaving_timestamp = get_ist_time().replace(tzinfo=None)
            total_seconds = (leaving_timestamp - parking_time).total_seconds()
            total_hours = max(total_seconds / 3600, 1)
            
            total_cost = round(total_hours * reservation.spot.lot.price_per_hour * 100, 0)
            reservation_order = {
                "currency": "INR",
                "amount": total_cost,
                "payment_capture": "1"
                
            }
            order = razorpay_client.order.create(data=reservation_order)
            reservation_data = {
                "reservation_id": reservation_id,
                "spot_id": reservation.spot_id,
                "vehicle_number":reservation.vehicle_number,
                "parking_time": parking_time.strftime('%Y-%m-%d %H:%M:%S'),
                "leaving_time": leaving_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "total_cost": total_cost
            }
            return {
                "order": order,
                "reservation_data": reservation_data
            }, 200
        return {"message": "Reservation ID is required!"}, 400
        
    @jwt_required()
    @role_required("user")
    def post(self):
        razorpay_client = razorpay.Client(auth=(current_app.config["RAZORPAY_CLIENT_ID"],current_app.config["RAZORPAY_ACCESS_KEY"]))
        data = request.get_json()
        reservation_id = data.get("reservation_id")
        order_id = data.get("order_id")
        payment_id = data.get("payment_id")
        signature = data.get("signature")
        parking_cost = data.get("amount")
        try:
            if reservation_id:
                reservation = Reservation.query.get_or_404(reservation_id) 
                if order_id and payment_id and signature:
                    payment_data = {
                        "razorpay_order_id": order_id,
                        "razorpay_payment_id": payment_id,
                        "razorpay_signature": signature
                    }
                    razorpay_client.utility.verify_payment_signature(payment_data)
                    payment = razorpay_client.payment.fetch(payment_id)
                    if payment["status"] == "captured":
                        reservation.payment_status = True
                        reservation.leaving_timestamp = get_ist_time()
                        reservation.spot.status = True
                        reservation.parking_cost = parking_cost
                        db.session.commit()
                        return {'message': 'Payment successful!'}, 200
                    return  {'message': 'Payment not successful.'}, 400
                return {"message":"Payment ID, Order ID and Signature are required!"}, 400
            return {"message":"Reservation ID is required!"}, 400
        except:
            return {'message': 'Something went wrong!'}, 500       
                    
                    
            
        
        

    # @jwt_required()
    # @role_required('Customer')    
    # def post(self):
    #     data = request.json
    #     required_fields = ['service_request_id', 'payment_id', 'order_id', 'signature']
    #     for field in required_fields:
    #         if not data.get(field):
    #             return f"{field} is required!", 400
    #     try:
    #         service_request_id = data['service_request_id']
    #         payment_id = data['payment_id']
    #         order_id = data['order_id']
    #         signature = data['signature']

    #         params_dict = {
    #             'razorpay_order_id': order_id,
    #             'razorpay_payment_id': payment_id,
    #             'razorpay_signature': signature
    #         }

    #         razorpay_client.utility.verify_payment_signature(params_dict)

    #         payment = razorpay_client.payment.fetch(payment_id)
    #         if payment['status'] == 'captured':
    #             service_request = ServiceRequest.query.get_or_404(service_request_id)
    #             service_request.payment_status = True
    #             db.session.commit()

    #             return {'message': 'Payment successful!'}, 200
    #         else:
    #             return {'message': 'Payment not successful.'}, 400

    #     except:
    #         return {'message': 'Something went wrong!'}, 500
        
        
        
        
        