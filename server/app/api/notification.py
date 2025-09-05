from flask_restful import Resource
from flask import request


from ..models import User, Notification
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.helper import role_required, lot_can_delete
from .. import db, cache

class NotificationApi(Resource):
    @jwt_required()
    @role_required("user")
    def get(self):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        notifications = Notification.query.filter_by(user_id=user.user_id).all()
        notification_detail = [{
            "notification_id": notification.notification_id,
            "title":notification.title,
            "body":notification.body
        } for notification in notifications]
        return notification_detail, 200