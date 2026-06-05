from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('ultrasound', 'Ultrasound'),
        ('xray', 'X-Ray'),
        ('pregnancy', 'Pregnancy Scan'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    class Inquiry(models.Model):

                 

        name = models.CharField(max_length=70)
        phone = models.CharField(max_length=20)
        inquiry_message = models.TextField(blank=True)
        date = models.DateTimeField(auto_now_add=True)




        
    

    # Its a Python class that defines the structure of your data, that is How your data looks
    # Allows you to manage data using python code instead of writing raw SQL
    # Database mapping - each model class maps to a single table in your database.
                       # and each attribute of a class rep a database field(column)
    # Django uses ORM (Object-Relational Mapper) to interact with the database 
         # Meaning one can CRUD(Create, Read, Update & Delete) records using python objects and methods
    # Inheritance - All models must sub-class django.db.models.Model