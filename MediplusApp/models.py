from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    phone_no = models.CharField(max_length=15, blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.name


class bookAppointment(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone_no = models.CharField(max_length=12, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    created_date = models.DateField(auto_now_add=True)
    department = models.CharField(
        max_length=100,
        choices=[
            ('Cardiology', 'Cardiology'),
            ("Neurology", "Neurology"),
            ("Orthopedics", "Orthopedics"),
            ("Pediatrics", "Pediatrics"),
            ("General Medicine", "General Medicine")
        ]
    )
    doctors_name = models.CharField(
        max_length=150,
        choices=[
            ('Dr.Uday Rasal', "Dr.Uday Rasal"),
            ("Dr.Payal Chavan", "Dr.Payal Chavan"),
            ("Dr.Trupti Kupekar", "Dr.Trupti Kupekar"),
            ("Dr.Ashish Sarule", "Dr.Ashish Sarule")
        ]
    )
    message = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    bookappointment = models.ManyToManyField(
        bookAppointment,
        blank=True,
        related_name='departments'  # Add a custom related_name
    )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    bookappointment = models.ForeignKey(
        bookAppointment,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='doctors'  # Add a custom related_name
    )

    def __str__(self):
        return self.name
