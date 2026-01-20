# Lab Manual: Django & PostgreSQL

**Objective**: Learn how to move from SQLite to PostgreSQL, understand database relationships, and write optimized queries.
**Duration**: 1.5 - 2 Hours

---

## Phase 0: Installation (15 Minutes)
*Goal: Ensure everyone has the database server running.*

### For Windows Users
1.  **Download**: Go to [postgresqltutorial.com](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/) or [enterprisedb.com](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
2.  **Run Installer**:
    *   **Password Step**: This is CRITICAL. **Write it down immediately.** You *will* need this later.
    *   **Port**: Default is `5432`.
3.  **Verify**: Search for "pgAdmin 4" in Start Menu and open it. If it asks for a password, it's working.

### For Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### For Mac
```bash
brew install postgresql
brew services start postgresql
```

---

## Phase 1: The Terminal & Raw SQL (30 Minutes)
*Goal: Understand that a database is just a place we send text commands to.*

### Step 1: Logging In
Open `cmd` or `PowerShell` (or Terminal).
```bash
# Try this command
psql -U postgres
```
*   *Note*: If you see "command not found", ask for help adding Postgres `bin` to your PATH, or open the **SQL Shell (psql)** app from your Start Menu.

### Step 2: Meta Commands
In `psql`, commands starting with `\` talk to the tool, not the database.
*   `\l` : **List** all databases.
*   `\du` : **Display Users**.
*   `\c db_name` : **Connect** to a specific database.

### Step 3: Challenge - Manual Creation
Let's create our database manually to understand what's happening under the hood. Type these commands carefully:

```sql
-- 1. Create the database
CREATE DATABASE school_db;

-- 2. Create a dedicated user (Best Practice)
CREATE USER school_admin WITH PASSWORD 'secret123';

-- 3. Give permissions
ALTER ROLE school_admin SET client_encoding TO 'utf8';
ALTER ROLE school_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE school_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE school_db TO school_admin;
```
*   *Verification*: Run `\l` again. Do you see `school_db`?

### Step 4: Raw SQL vs ORM
Connect to your new DB: `\c school_db`

Let's try creating a table the "hard way" to appreciate what Django does for us:
```sql
-- Create a table manually
CREATE TABLE temp_student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
);

-- Insert data
INSERT INTO temp_student (name, age) VALUES ('Alice', 20);
INSERT INTO temp_student (name, age) VALUES ('Bob', 22);

-- Read data
SELECT * FROM temp_student;
```
*Takeaway*: Typing this for complex tables is error-prone. Django automates this.

---

## Phase 2: Connecting Django (20 Minutes)
*Goal: Connect our application to the server we just set up.*

### Step 1: Drivers & Environment
Stop your Django server. In your terminal, install the necessary packages:
```bash
pip install psycopg2-binary python-dotenv
```

### Step 2: The `.env` File
Create a new file named `.env` in the project root folder. Add your database credentials:
```env
DB_NAME=school_db
DB_USER=postgres
DB_PASSWORD=your_password  <-- The password you wrote down in Phase 0
DB_HOST=localhost
DB_PORT=5432
```

### Step 3: Update Settings.py
Open `core/settings.py`.
1.  Add these imports at the top:
    ```python
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ```
2.  Replace the `DATABASES` section with:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
    ```

### Step 4: validtation
Run the migration command:
```bash
python manage.py migrate
```
*   *Verification*: Go back to your `psql` terminal and type `\dt`.
    *   You should see tables like `auth_user`, `django_session`, etc.
    *   Django just wrote all that SQL for us!

---

## Phase 3: The Refactor (Foreign Keys) (30 Minutes)
*Goal: Move from simple "Strings" to "Relationships".*

### The Problem
Look at `routine/models.py`.
`teacher = models.CharField(max_length=100)`
*   What if "Mr. John" changes his name?
*   What if you make a typo like "Mr. Jon"? (The data won't match)

### The Fix
Modify `routine/models.py` to use a **ForeignKey**:

```python
from members.models import Member

class Routine(models.Model):
    # ... (keep other fields) ...
    
    # OLD: teacher = models.CharField(max_length=100)
    
    # NEW:
    teacher = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE,
        limit_choices_to={'member_type': 'teacher'}, # Only show teachers!
        related_name='routines'
    )
    
    # ...
```

### Constraints (Data Integrity)
Let's prevent double-booking a room. Add this to the `Meta` class in `Routine`:
```python
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['day', 'start_time', 'room'], 
                name='unique_room_booking'
            )
        ]
```

### Apply Changes
```bash
python manage.py makemigrations
python manage.py migrate
```
*   *Note*: Since we switched to a fresh PostgreSQL database, the `routine` table is empty, so this migration should run smoothly.

---

## Phase 4: ORM Power & Optimization (25 Minutes)
*Goal: Write efficient queries reducing database load.*

Open the Django Shell to experiment: `python manage.py shell`

### 1. Creating Data (The Python Way)
```python
from members.models import Member
from routine.models import Routine
import datetime

# Create a teacher
t = Member.objects.create(name="Prof. X", member_type="teacher", email="x@school.com")

# Create a routine linked to that teacher
Routine.objects.create(
    day="monday",
    class_name="Class 10",
    subject="Physics",
    teacher=t,  # <--- Passing the OBJECT, not a string
    start_time=datetime.time(10,0),
    end_time=datetime.time(11,0),
    room="101"
)
```

### 2. The N+1 Problem (Optimization)
**Scenario**: We want to list all routines and the name of the teacher for each.

**The Slow Way (N+1)**:
```python
# 1. Django hits DB to get all routines (1 query)
routines = Routine.objects.all() 

for r in routines:
    # 2. Django hits DB AGAIN for EVERY routine to find the teacher's name
    print(r.teacher.name) 
```
*   If you have 1000 routines, this runs 1001 database queries!

**The Optimized Way (Select Related)**:
```python
# 1. Django does a SQL JOIN. Fetches everything in 1 single query.
routines = Routine.objects.select_related('teacher').all()

for r in routines:
    print(r.teacher.name) # Data is already here. 0 extra queries.
```

### 3. Inspecting the SQL
Want to see the magic? Run this:
```python
qs = Routine.objects.select_related('teacher')
print(str(qs.query))
```
*   You will see the raw `SELECT ... INNER JOIN ...` SQL command that Django generated.

---

## Checklist
- [ ] PostgreSQL installed & running?
- [ ] `.env` file created and hidden from Git?
- [ ] `Routine` model updated to use `ForeignKey`?
- [ ] `select_related` used for fetching related data?
