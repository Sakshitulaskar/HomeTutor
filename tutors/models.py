from django.db import models
from django.contrib.auth.models import User



class Tutor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    subject = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=200
    )

    experience = models.IntegerField()

    fees = models.IntegerField()

    availability = models.CharField(
        max_length=100
    )

    mode = models.CharField(
        max_length=50
    )

    city = models.CharField(
        max_length=100
    )

    area = models.CharField(
        max_length=100
    )

    image = models.ImageField(
        upload_to='tutors/'
    )

    def __str__(self):

        return self.user.username




class Review(models.Model):

    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.student.username