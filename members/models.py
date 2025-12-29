from django.db import models

class Member(models.Model):
    MEMBER_TYPE = (
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    
    member_type = models.CharField(max_length=10,choices = MEMBER_TYPE)
    
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    photo = models.ImageField(upload_to='members_photo')
    
    def __str__(self):
        return self.name
