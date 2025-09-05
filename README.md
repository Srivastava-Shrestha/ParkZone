# ParkZone


## 💻 Built with

### Backend
- **Flask**: A web framework.
- **Flask_SQLAlchemy**: Manages database operations.
- **Flask-JWT-Extended**: For handling JSON Web Tokens.
- **Flask_RESTful**: Simplifies creating REST APIs.
- **Flask-Caching**: Adds caching support.
- **Celery**: Handles asynchronous tasks.
- **Redis**: Message broker and caching layer.
- **Razorpay**: Integrates payment gateway.

### Database
- **SQLite**: A lightweight database.

### Frontend
- **HTML**: For structuring web pages.
- **CSS**: Styles web pages.
- **JavaScript**: Adds interactivity.
- **VueJS**: Builds dynamic, reactive user interfaces.
- **Vite**: Provides fast development environment for VueJS.
- **Bootstrap**: For responsive and mobile-first design.
- **ChartJS**: Visualizes data through charts.

## ⚙️ Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/23f3000168/ParkZone.git
```

### 2. Change the working directory
```bash
cd ParkZone
```

### 3. Create & Activate Virtual Environment
- #### Create Virtual Environment
  
```bash
cd server
python -m venv venv
```

- #### Activate Virtual Environment
For Linux/macOS:
```
source venv/bin/activate
```
For Windows:
```
venv\\Scripts\\activate
```

### 4. Install Required Backend Package Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Backend
```bash
python run.py
```

### 6. Install Frontend Dependencies
In a new terminal window, install frontend dependencies:
```bash
cd ../client
npm install
```

### 7. Run the Frontend Development Server
```bash
npm run dev
```

### 8. Setup Redis
Make sure Redis is installed and running. You can start Redis using:
```bash
redis-server
```

### 9. Run Celery Worker
In a new terminal window, run the Celery worker:
```bash
cd ../server
celery -A run.celery worker --loglevel=info
```

### 10. Run Celery Beat
In another terminal window, run the Celery Beat scheduler:
```bash
celery -A run.celery beat --loglevel=info
```

 You are all set!
<hr>
<h3 align="center">
Thank You 
</h3>
