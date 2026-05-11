from django.urls import path
from . import views

urlpatterns = [

    path(
        'tutors/',
        views.tutors_page,
        name='tutors'
    ),
    path(
    'tutor/<int:tutor_id>/',
    views.tutor_detail,
    name='tutor_detail'
    ),

    path(
    'create-tutor-profile/',
    views.create_tutor_profile,
    name='create_tutor_profile'
    ),
]