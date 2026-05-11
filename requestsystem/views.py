from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from tutors.models import Tutor

from .models import TuitionRequest



@login_required
def send_request(request, tutor_id):

    tutor = Tutor.objects.get(id=tutor_id)

    if request.method == 'POST':

        message = request.POST['message']

        TuitionRequest.objects.create(
            student=request.user,
            tutor=tutor,
            message=message
        )

        return redirect('tutors')

    return render(
        request,
        'send_request.html',
        {'tutor': tutor}
    )

@login_required
def tutor_requests(request):

    tutor = Tutor.objects.filter(
        user=request.user
    ).first()

    if not tutor:

        return redirect('tutors')

    requests = TuitionRequest.objects.filter(
        tutor=tutor
    )

    return render(
        request,
        'tutor_requests.html',
        {'requests': requests}
    )

@login_required
def accept_request(request, request_id):

    req = TuitionRequest.objects.get(id=request_id)

    req.status = 'Accepted'

    req.save()

    return redirect('tutor_requests')

@login_required
def reject_request(request, request_id):

    req = TuitionRequest.objects.get(id=request_id)

    req.status = 'Rejected'

    req.save()

    return redirect('tutor_requests')

@login_required
def student_requests(request):

    requests = TuitionRequest.objects.filter(
        student=request.user
    )

    return render(
        request,
        'student_requests.html',
        {'requests': requests}
    )