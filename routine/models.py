from django.db import models


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
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.day})"
