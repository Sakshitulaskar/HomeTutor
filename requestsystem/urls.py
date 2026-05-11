from django.urls import path
from . import views

urlpatterns = [

    path(
        'send-request/<int:tutor_id>/',
        views.send_request,
        name='send_request'
    ),

    path(
        'tutor-requests/',
        views.tutor_requests,
        name='tutor_requests'
    ),

    path(
        'accept-request/<int:request_id>/',
        views.accept_request,
        name='accept_request'
    ),

    path(
        'reject-request/<int:request_id>/',
        views.reject_request,
        name='reject_request'
    ),
    
    path(
    'student-requests/',
    views.student_requests,
    name='student_requests'
    ),
]