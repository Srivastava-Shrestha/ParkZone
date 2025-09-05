#ParkZone/server/run.py

from app import app_creator
from app.config import Configuration

app, celery = app_creator(Configuration)

if __name__ == "__main__":
    app.run(debug=True,port=1437)