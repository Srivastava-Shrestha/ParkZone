# ParkZone
ParkZone is a multi-user platform that helps admins manage parking lots and spots while allowing users to easily reserve, occupy, and release spaces. It features dashboards, real-time spot availability, automated allocation, reminders, and activity reports for smooth and efficient parking management.

![ParkZone1](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone1.png)

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
- **SQLite**: A lightweight database.

### Frontend
- **HTML**: For structuring web pages.
- **CSS**: Styles web pages.
- **JavaScript**: Adds interactivity.
- **VueJS**: Builds dynamic, reactive user interfaces.
- **Vite**: Provides fast development environment for VueJS.
- **Bootstrap**: For responsive and mobile-first design.
- **Lucide-Icons**: Provides a wide set of customizable icons.
- **ChartJS**: Visualizes data through charts.

## ⚙️ Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Srivastava-Shrestha/ParkZone.git
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

🌟 You are all set!
<hr>

## 📸 Screenshots
![ParkZone2](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone2.png)
![ParkZone3](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone3.png)
![ParkZone4](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone4.png)
![ParkZone5](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone5.png)
![ParkZone6](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone6.png)
![ParkZone7](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone7.png)
![ParkZone8](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone8.png)
![ParkZone9](https://github.com/Srivastava-Shrestha/Assets/blob/main/ParkZone/ParkZone9.png)


<hr>
<h3 align="center">
Thank You 🐻
</h3>
