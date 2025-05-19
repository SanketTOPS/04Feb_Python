from django.db import models


# Create your models here.
class Usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()


class Notes(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(Usersignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    notefile = models.FileField(upload_to="NotesFiles")
    statuschoice = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]
    status = models.CharField(max_length=10, choices=statuschoice)
    updated_at = models.DateTimeField(blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
