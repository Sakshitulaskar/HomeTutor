from django.db import models

from django.contrib.auth.models import User

from tutors.models import Tutor


class TuitionRequest(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),

        ('Accepted', 'Accepted'),

        ('Rejected', 'Rejected'),

    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.student.username