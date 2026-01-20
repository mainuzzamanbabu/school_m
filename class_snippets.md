# Class Snippets & Commands
*Use these snippets during your 1.5 - 2 hour class.*

## 1. Install PostgreSQL Adapter & Dotenv
Command to run in terminal:
```bash
pip install psycopg2-binary python-dotenv
```

## 2. Django Settings (`settings.py`)
Add this to the top of `settings.py`:
```python
import os
from dotenv import load_dotenv
load_dotenv()
```

Replace the `DATABASES` block with this:
```python
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

## 3. Create .env File
Create a file named `.env` next to `manage.py`:
```env
DB_NAME=school_db
DB_USER=postgres
DB_PASSWORD=secret
DB_HOST=localhost
```

## 3. The "Bad" Routine Model (Current State)
*Reference only - this is what you likely have now.*
```python
class Routine(models.Model):
    # ... other fields ...
    teacher = models.CharField(max_length=100) # Simple text - prone to errors
```

## 4. The "Better" Routine Model (Refactor)
*Update `routine/models.py` to use ForeignKey.*

```python
from members.models import Member # Import the Member model

class Routine(models.Model):
    DAY_CHOICES = (
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    class_name = models.CharField(max_length=50, help_text="e.g., Class 10-A, HSC-Science")
    subject = models.CharField(max_length=100)
    
    # NEW: Link to Member model, only pick teachers
    teacher = models.ForeignKey(
        Member, 
        on_delete=models.CASCADE,
        limit_choices_to={'member_type': 'teacher'},
        related_name='routines'
    )
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['day', 'start_time']
        # NEW: Prevent double booking of the same room at the same time
        constraints = [
            models.UniqueConstraint(
                fields=['day', 'start_time', 'room'], 
                name='unique_room_booking'
            )
        ]

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.day})"
```

## 5. Optimized Query (Views Examples)
*Demonstrate in `django shell` or a `views.py`*

**The Problem (N+1)**:
```python
# Fetches routines, then hits DB again for EACH teacher
routines = Routine.objects.all()
for r in routines:
    print(r.teacher.name) 
```

**The Solution (`select_related`)**:
```python
# Fetches routines + teachers in 1 single query
routines = Routine.objects.select_related('teacher').all()
for r in routines:
    print(r.teacher.name)
```

## 6. Helpful Shell Commands
Open the Django shell to test queries interactively:
```bash
python manage.py shell
```

Test the constraint (inside shell):
```python
from routine.models import Routine
from datetime import time

# Try to create duplicates to see the error
# (Assuming you created a routine in the admin already)
r = Routine(day='monday', start_time=time(10,0), room='101')
r.save() # Should crash if conflicting
```
