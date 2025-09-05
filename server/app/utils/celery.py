from celery import Celery
from celery.schedules import crontab
from flask import current_app

celery = Celery("ParkZone Async Jobs", include="app.utils")

def init_celery(app):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with current_app.app_context():
                return self.run(*args, **kwargs)
            
    celery.conf.update(broker_url=app.config["CELERY_BROKER_URL"], result_backend=app.config["CELERY_RESULT_BACKEND"])
    celery.Task = ContextTask
    app.app_context().push()

    celery.conf.timezone = 'Asia/Kolkata'

    return celery

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from .daily import daily_remainder
    sender.add_periodic_task(
        crontab(minute='55', hour='16'),
        daily_remainder.s(),
        name='daily_task'
    )
    from .monthly import monthly_remainder
    sender.add_periodic_task(
        crontab(minute='22', hour='17', day_of_month='30'),
        monthly_remainder.s(),
        name='monthly_task'
    )

