from .. import db

class Notification(db.Model):
    __tablename__="notification"
    notification_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.Text, nullable=False)
    
    user = db.relationship("User", back_populates="notifications", uselist=False)