# ParkZone/server/app/api/lot.py

from ctypes import addressof
from flask_restful import Resource
from flask import request
from ..models import Lot, Spot
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.helper import role_required, lot_can_delete
from .. import db, cache


class LotApi(Resource):
    @jwt_required()
    @role_required("admin")
    def post(self):
        cache.clear()
        data = request.get_json()
        prime_location = data.get("prime_location")
        price_per_hour = data.get("price_per_hour")
        address = data.get("address")
        pincode = data.get("pincode")
        no_of_spots = data.get("no_of_spots")

        if prime_location is None or prime_location == "":
            return {"message": "prime_location is required!"}, 400
        if price_per_hour is None or price_per_hour == "":
            return {"message": "price_per_hour is required!"}, 400
        if address is None or address == "":
            return {"message": "address is required!"}, 400
        if pincode is None or pincode == "":
            return {"message": "pincode is required!"}, 400
        if no_of_spots is None or no_of_spots == "":
            return {"message": "no_of_spots is required!"}, 400
        
        try:
            new_lot = Lot(prime_location=prime_location,price_per_hour=price_per_hour,address=address,pincode=pincode,no_of_spots=no_of_spots)
            db.session.add(new_lot)
            db.session.flush()
            for i in range(no_of_spots):
                new_spot = Spot(lot_id=new_lot.lot_id)
                db.session.add(new_spot)
            db.session.commit()
            return {"message": "Parking Lot added succesfully!"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"Something went wrong!"}, 500
        
    @jwt_required()
    @cache.cached(timeout=60, query_string=True)
    def get(self,lot_id=None):
        try:
            if lot_id is None:
                query = Lot.query
                parameters = request.args
                name = parameters.get("name")
                if name:
                    query = query.filter(Lot.prime_location.ilike(f"%{name}%"))
                pincode = parameters.get("pincode")
                if pincode:
                    query = query.filter(Lot.pincode.ilike(f"%{pincode}%"))
                address = parameters.get("address")
                if address:
                    query = query.filter(Lot.address.ilike(f"%{address}%"))
                all_lots = query.all()
                lot_details = [{
                "lot_id": lot.lot_id,
                "prime_location": lot.prime_location,
                "price_per_hour": lot.price_per_hour,
                "address": lot.address,
                "pincode": lot.pincode,
                "no_of_spots": lot.no_of_spots,
                "spots":[{
                        "spot_id":spot.spot_id,
                        "status":spot.status
                    } for spot in lot.spots]}
                      for lot in all_lots]
                return lot_details, 200
            else:
                lot = Lot.query.filter_by(lot_id = lot_id).first()
                if lot:
                    lot_detail = {
                        "lot_id": lot.lot_id,
                    "prime_location": lot.prime_location,
                    "price_per_hour": lot.price_per_hour,
                    "address": lot.address,
                    "pincode": lot.pincode,
                    "no_of_spots": lot.no_of_spots,
                    "spots":[{
                        "spot_id":spot.spot_id,
                        "status":spot.status
                    }for spot in lot.spots]}
                    return lot_detail, 200
                else:
                    return {"message": "Parking Lot not found"}, 400
                
        except Exception as e:
            return {"message": f"Something went wrong!"}, 500



    @jwt_required()
    @role_required("admin")
    def put(self, lot_id):
        cache.clear()
        try:
            data = request.get_json()
            lot = Lot.query.filter_by(lot_id=lot_id).first()

            if not lot:
                return {"message": "Parking Lot not found!"}, 404

            lot.prime_location = data.get("prime_location", lot.prime_location)
            lot.price_per_hour = data.get("price_per_hour", lot.price_per_hour)
            lot.address = data.get("address", lot.address)
            lot.pincode = data.get("pincode", lot.pincode)

            db.session.commit()
            return {"message": "Parking Lot updated successfully!"}, 200
        
        except Exception as e:
            db.session.rollback()
            return {"message": f"Something went wrong! "}, 500


    @jwt_required()
    @role_required("admin")
    def delete(self, lot_id):
        cache.clear()
        try:
            lot = Lot.query.filter_by(lot_id=lot_id).first()


            if lot:
                if lot_can_delete(lot):
                    db.session.delete(lot)
                    db.session.commit()
                    return {"message":"Parking lot deleted successfully!"}, 200
                else:
                    return {"message":"This Parking Lot cannot be deleted. One or more spots are occupied!"}, 400
            else:
                return {"message":"Parking lot not found!"}, 400
            
        except:
            db.session.rollback()
            return {"message":"Something went wrong!"}, 500