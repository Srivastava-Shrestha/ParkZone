# ParkZone/server/app/api/spot.py

from flask_restful import Resource
from flask import request
from ..models import Lot, Spot
from flask_jwt_extended import jwt_required
from ..utils.helper import role_required
from .. import db, cache


class SpotApi(Resource):
    @jwt_required()
    @role_required("admin")
    def put(self, spot_id):
        cache.clear()
        data = request.get_json()
        new_status = data.get("status")
        try:
            if not isinstance(new_status, bool):
                return {"message": "Invalid status."}, 400
            
            spot_exist = Spot.query.filter_by(spot_id=spot_id).first()

            if spot_exist:
                spot_exist.status = new_status
                db.session.commit()
                return {"message": "Spot status updated successfully."}, 200
            else:
                return {"message": "Parking Spot not found."}, 404
            
        except:
            db.session.rollback()
            return {"message":"Something went wrong!"}, 500

    @jwt_required()
    @role_required("admin")
    def delete(self, spot_id):
        cache.clear()
        try:
            spot = Spot.query.filter_by(spot_id=spot_id).first()
            if spot:
                lot_id = spot.lot_id
                lot = Lot.query.filter_by(lot_id=lot_id).first()
                if spot.status is True:
                    db.session.delete(spot)
                    lot.no_of_spots -= 1
                    db.session.commit()
                    return {"message":"Parking Spot deleted successfully!"}, 200
                else:
                    return {"message":"This Parking Spot is occupied, so it can't be deleted!"}, 400
            else:
                return {"message":"Parking Spot not found!"}, 400
            
        except Exception as e:
            db.session.rollback()
            return {"message":f"Something went wrong!{e}"}, 500


