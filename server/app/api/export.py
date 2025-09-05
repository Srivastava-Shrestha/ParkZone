from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.helper import role_required
from ..utils.task import export_user_usage_csv
from flask_restful import Resource
from ..models import User

class ExportApi(Resource):
    @jwt_required()
    @role_required("user")
    def get(self):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        result = export_user_usage_csv.delay(user.user_id, user.email)
        return {"message":"CSV will be send Soon", "result_id":result.id}, 200
        
        
        