#ParkZone/server/app/__init__.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from .utils.celery import init_celery
from flask_caching import Cache

app = Flask(__name__)
db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()
cache = Cache()

def app_creator(MyConfig):

    app.config.from_object(MyConfig)
    db.init_app(app)
    api = Api(app)
    jwt.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    CORS(app,  supports_credentials=True)
    
    from .models import Admin,User,Lot,Spot,Reservation, Notification

    with app.app_context():
        db.create_all()

        if not Admin.query.filter_by(username="shrestha").first():
            admin = Admin(username = "shrestha", email="shrestha30@gmail.com")
            admin.hash_password("shrestha30")
            db.session.add(admin)
            db.session.commit()

        
    
        


    from .api import  SignupApi, LoginApi, LotApi, SpotApi, ReservationApi, UserApi, PaymentApi, StatsApi, NotificationApi, ExportApi
    
    api.add_resource(SignupApi, "/api/signup")
    api.add_resource(LoginApi, "/api/login")
    api.add_resource(LotApi, "/api/lot", "/api/lot/<int:lot_id>")
    api.add_resource(SpotApi, "/api/spot/<int:spot_id>")
    api.add_resource(ReservationApi, "/api/reservation", "/api/reservation/spot/<int:spot_id>", "/api/reservation/<int:reservation_id>")
    api.add_resource(UserApi, "/api/user", "/api/user/<int:user_id>")
    api.add_resource(PaymentApi, "/api/payment")
    api.add_resource(StatsApi, "/api/stats")
    api.add_resource(NotificationApi, "/api/notification")
    api.add_resource(ExportApi, "/api/export")
    
    celery = init_celery(app)
    
    return app, celery