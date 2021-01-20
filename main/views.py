# class based views
from django.views.generic.edit import UpdateView
# modules
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib import messages
from school_app.models import School
from school_app.forms import SchoolRegForm, SchoolRegForm2
from accounts.models import User, Profile
from .forms import PersonalRegForm
from teacher_app.models import Worker

def index(request):
    return render(request, 'home/index.html')


def preference(request):
    return render(request, 'main/preference.html')


def contactus(request):
    return render(request, 'main/contact-us.html')


def aboutus(request):
    return render(request, 'main/about.html')


def service(request):
    return render(request, 'main/service.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def school_registration(request):

    if request.method == 'POST':
        form = SchoolRegForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            data = form.save(commit=False)
            data.maintainer = request.user
            data.save()
            school = School.objects.get(name=name)
            worker = Worker.objects.get_or_create(person=request.user, school=school)
            # worker.school = school
            return redirect(f'/school/registration/personal/{request.user.id}')
    form = SchoolRegForm()
    context = {
        'form': form
    }
    return render(request, 'school/school_registration/school_form1.html', context)


@transaction.atomic
def update_personal(request, id):
    user = User.objects.get(id=id)
    worker = Worker.objects.get(person=user)
    if request.user != user:
        return redirect('index')

    if request.method == 'POST':
        form = PersonalRegForm(
            request.POST, instance= user.profile)
        if form.is_valid():
            form.save()
            is_admin = form.cleaned_data.get('are_you_admin')
            if not user.school_owner:
                if is_admin:
                    user.school_owner = True
                    user.save()
            # return redirect(reverse('accounts', kwargs={'username': user.username}))
            messages.success(
                request,
                'Your Profile was successfully updated!!'
            )

            return redirect(f'/school/registration/{worker.school.id}')
        else:
            messages.error(request, 'please correct the error below.')
    else:
        form = PersonalRegForm(instance=user.profile)
        return render(request, 'school/school_registration/personal_form.html', {'profile_form': form})


class SchoolRegView(UpdateView):
    model = School
    fields = ['slug']
    template_name = 'school/school_registration/cont_form.html'
    success_url = '/school/registration/congrats'


def success_message(request):
    user = User.objects.get(username=request.user.username)
    worker = Worker.objects.get(person=user)
    school = School.objects.get(name=worker.school.name)
    context = {
        'user':user,
        'worker':worker,
        'school':school
    }
    return render(request, 'school/school_registration/congrats_msg.html', context)




def course(request):
    return render(request, 'school/school_admin/course/course.html')


def class_detail(request):
    return render(request, 'school/school_admin/course/class_detail.html')

def testing12(request):
    return render(request, 'school/school_admin/web_edit/home_edit.html')


def testing13(request):
    return render(request, 'school/school_admin/gallery/gallery.html')


def testing14(request):
    return render(request, 'school/school_admin/forms/register_students.html')
