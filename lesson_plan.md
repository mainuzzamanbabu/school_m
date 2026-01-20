# Lesson Plan: Django Database Mastery with PostgreSQL
**Duration**: 1.5 - 2 Hours
**Target Audience**: Students familiar with basic Django (Views, Templates, Urls).

## 1. Introduction: Why PostgreSQL? (15 Minutes)
Start by explaining why we are moving away from SQLite.
*   **SQLite**: File-based, great for dev, locks the whole file on write (bad for concurrency), limited data types.
*   **PostgreSQL**: Server-based, robust, production-standard, huge concurrency, advanced data types (JSONB, Array), strict integrity.

**Visual Metaphor**: SQLite is like a single notebook everyone shares (one person writes at a time). PostgreSQL is like a library with a team of librarians managing requests simultaneously.

## 2. Practical: Connecting Django to PostgreSQL (20 Minutes)
*Goal: Switch the existing project from SQLite to Postgres.*

### Prerequisites
*   Ensure PostgreSQL is installed.
*   Library needed: `psycopg2` (or `psycopg2-binary`).

### Steps to Show
1.  **Create Database**: Open pgAdmin or terminal and create a new DB `school_db`.
2.  **Install Drivers & Dotenv**: `pip install psycopg2-binary python-dotenv`
3.  **Create .env file**:
    *   Create a file named `.env` in the root (same level as `manage.py`).
    *   Add specific values:
        ```env
        DB_NAME=school_db
        DB_USER=postgres
        DB_PASSWORD=secret
        DB_HOST=localhost
        ```
4.  **Update settings.py**:
    *   Import `os` and load dotenv at the top.
    *   Use `os.getenv()` for secrets.
    ```python
    import os
    from dotenv import load_dotenv
    
    load_dotenv() # Load variables from .env

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': '5432',
        }
    }
    ```
5.  **Migrate**: Run `python manage.py migrate`. Explain this builds the schema in the new empty DB using the secure credentials.

## 3. Core Concept: Relationships & Foreign Keys (30 Minutes)
*Goal: Fix a design flaw in the current `Routine` model to teach Relational Database concepts.*

**The Problem**: Currently, `Routine` has `teacher = models.CharField`.
*   *Discussion*: If "Mr. Smith" changes his name or leaves, we have to find/replace text everywhere. Typographical errors ("Mr. Smit") break queries.

**The Solution**: Link `Routine` to the `Member` app.

### Live Coding
1.  Open `routine/models.py`.
2.  Import `Member`: `from members.models import Member`.
3.  Change the field:
    ```python
    # old
    # teacher = models.CharField(max_length=100)

    # new
    teacher = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE, 
        limit_choices_to={'member_type': 'teacher'}, # specific constraint
        related_name='routines' # reverse relationship name
    )
    ```
4.  **Constraint Explanation**: Explain `limit_choices_to`. It ensures we can't accidentally assign a student or admin as a teacher.
5.  **Migration Strategy**:
    *   Since we are changing a CharField to a ForeignKey, Django will ask what to do with existing data.
    *   *Teaching Moment*: In a fresh DB (which we just made in step 2), this is easy. In a production DB, this requires a clear migration plan (providing a default).

## 4. Advanced: Constraints & Integrity (15 Minutes)
*Goal: Prevent bad data at the database level.*

**Scenario**: Two classes cannot happen in the "Room 101" at "10:00 AM" on "Monday".

### Live Coding
Add a `UniqueConstraint` in `Routine` model `Meta` class.

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['day', 'start_time', 'room'], 
            name='unique_booking'
        )
    ]
```
*   Run `makemigrations` and `migrate`.
*   **Demonstrate**: Go to Admin panel, try to book a conflict. Watch the database reject it.

## 5. Performance: The N+1 Problem (20 Minutes)
*Goal: Show why `select_related` matters.*

**Scenario**: Showing a list of routines and their teachers.

1.  **The Bad Way**:
    ```python
    # views.py
    routines = Routine.objects.all()
    # template
    # {% for r in routines %}{{ r.teacher.name }}{% endfor %}
    ```
    *   *Explain*: If you have 100 routines, Django hits the DB 101 times (1 for list, 100 for each teacher lookup). Show the SQL logs (using `django-debug-toolbar` or `connection.queries` if time permits, or just explain conceptually).

2.  **The Good Way**:
    ```python
    # views.py
    routines = Routine.objects.select_related('teacher').all()
    ```
    *   *Explain*: This does a SQL `JOIN`. Fetches everything in 1 query.

## 6. Wrap up (10 Minutes)
*   Review `settings.py` changes.
*   Review the importance of `ForeignKey` vs simple text fields.
*   Recap constraints for data safety.
