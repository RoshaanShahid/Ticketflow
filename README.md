🎫 TicketFlow

TicketFlow is a web-based ticket booking platform built with Django. It allows users to browse events, select seats, and book tickets online. Admins can manage events, venues, and bookings through a secure admin panel.

📋 Features

User authentication (Sign up, login, logout)

Browse and search events

Book tickets and select seats

View booking history

Admin panel to manage:

Events

Venues

Tickets

Users

🛠️ Tech Stack

Backend: Django (Python)

Database: SQLite (default) / PostgreSQL (production recommended)

Frontend: React

Other Tools: Git & GitHub for version control

📁 Project Structure
ticketflow/
│
├── ticketflowProject/ # Main Django project folder
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── events/ # Django app for event and ticket logic
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
│
├── templates/ # Shared HTML templates
├── static/ # Static files (CSS, JS, Images)
│
├── db.sqlite3
├── manage.py
└── README.md

⚙️ Installation
Follow these steps to run the project locally:

1. Clone the repository
git clone [https://github.com/your-username/TicketFlow.git](https://github.com/your-username/TicketFlow.git)
cd TicketFlow

2. Create a virtual environment
python -m venv venv

3. Activate the environment
Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run migrations
python manage.py migrate

6. Create a superuser (admin)
python manage.py createsuperuser

7. Run the development server
python manage.py runserver

🚀 Usage
Open your browser and go to http://127.0.0.1:8000/.

Log in using your admin credentials at /admin.

Create events, venues, and tickets in the admin panel.

Users can register, browse events, and book tickets.

📦 Deployment
For production deployment, use:

Gunicorn / uWSGI as WSGI server

Nginx or Apache HTTP Server as reverse proxy

PostgreSQL as database

Docker (optional) for containerization

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Your Name
GitHub • LinkedIn
