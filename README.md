# SCL - School Management System

A Django-based school management application with features for managing members, notices, and routines.

## Features

- **Members Management** - CRUD operations for school members (Teachers, Staff, Students)
- **Notice Board** - Create, view, edit, and delete notices
- **Routine Management** - Manage school routines and schedules

## Tech Stack

- **Python** 3.x
- **Django** 4.2.27
- **SQLite** (default database)
- **Pillow** (for image processing)

---

## Setup Instructions

### Prerequisites

- Python 3.10 or higher installed on your system
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd SCL
```

### Step 2: Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional - for Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin username, email, and password.

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## Project Structure

```
SCL/
├── core/               # Main Django project settings
│   ├── settings.py     # Project configuration
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI configuration
├── members/            # Members app
│   ├── models.py       # Member model
│   ├── views.py        # Member views (CRUD)
│   └── admin.py        # Admin configuration
├── notice/             # Notice app
│   ├── models.py       # Notice model
│   ├── views.py        # Notice views (CRUD)
│   └── admin.py        # Admin configuration
├── routine/            # Routine app
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---

## Available URLs

| URL                     | Description        |
| ----------------------- | ------------------ |
| `/admin/`               | Django Admin Panel |
| `/members/`             | Members List       |
| `/members/create/`      | Create New Member  |
| `/members/<id>/`        | Member Details     |
| `/members/<id>/update/` | Update Member      |
| `/members/<id>/delete/` | Delete Member      |
| `/notices/`             | Notices List       |
| `/notices/create/`      | Create New Notice  |
| `/notices/<id>/`        | Notice Details     |
| `/notices/<id>/update/` | Update Notice      |
| `/notices/<id>/delete/` | Delete Notice      |

---

## Common Commands

```bash
# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

---

## License

This project is for educational purposes.
