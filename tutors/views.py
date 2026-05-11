from django.shortcuts import render, redirect

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from .models import Tutor, Review
from accounts.models import Profile



def tutors_page(request):

    tutors = Tutor.objects.all()

    search = request.GET.get('search')

    max_fees = request.GET.get('max_fees')

    min_experience = request.GET.get('min_experience')

    city = request.GET.get('city')

    area = request.GET.get('area')


    if search:

        tutors = tutors.filter(

            Q(subject__icontains=search) |

            Q(user__username__icontains=search)

        )


    if max_fees:

        tutors = tutors.filter(
            fees__lte=max_fees
        )


    if min_experience:

        tutors = tutors.filter(
            experience__gte=min_experience
        )


    if city:

        tutors = tutors.filter(
            city__icontains=city
        )


    if area:

        tutors = tutors.filter(
            area__icontains=area
        )


    return render(
        request,
        'tutors.html',
        {
            'tutors': tutors
        }
    )



@login_required
def tutor_detail(request, tutor_id):

    tutor = Tutor.objects.get(id=tutor_id)

    reviews = Review.objects.filter(
        tutor=tutor
    )


    if request.method == 'POST':

        rating = request.POST['rating']

        comment = request.POST['comment']

        Review.objects.create(
            tutor=tutor,
            student=request.user,
            rating=rating,
            comment=comment
        )

        return redirect(
            'tutor_detail',
            tutor_id=tutor.id
        )


    return render(
        request,
        'tutor_detail.html',
        {
            'tutor': tutor,
            'reviews': reviews
        }
    )

@login_required
def create_tutor_profile(request):

    profile = Profile.objects.filter(
     user=request.user
    ).first()
    if not profile:

      return redirect('register')

    if profile.role != 'Tutor':

        return redirect('home')


    if request.method == 'POST':

        subject = request.POST['subject']

        qualification = request.POST['qualification']

        experience = request.POST['experience']

        fees = request.POST['fees']

        availability = request.POST['availability']

        mode = request.POST['mode']

        city = request.POST['city']

        area = request.POST['area']

        image = request.FILES['image']


        Tutor.objects.create(

            user=request.user,

            subject=subject,

            qualification=qualification,

            experience=experience,

            fees=fees,

            availability=availability,

            mode=mode,

            city=city,

            area=area,

            image=image

        )

        return redirect('tutors')


    return render(
        request,
        'create_tutor_profile.html'
    )