from django.shortcuts import render


# Create your views here.
from dj03 import settings
from django.core.mail import send_mail
from newsletter.models import SignUp
from .forms import SignUpForm, ContactUsForm


def HomeView(request):
    title = "Welcome "

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'title': title,
        'form': form,
    }

    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset" : queryset,
        }
    return render(request, 'home.html', context)



def ContactView(request):
    form_c = ContactUsForm(request.POST or None)

    if form_c.is_valid():
        full_Name = form_c.cleaned_data.get('full_name')
        subject = form_c.cleaned_data.get('subject')
        msg = 'Your message has been received. We will contact you asap.'
        sub = 'Subject: sample mail'

        send_mail(
            sub,
            msg,
            settings.EMAIL_HOST_USER,
            ['kumar.priyam55@gmail.com'],
            fail_silently=False,
        )

    context = {
          'form_c' : form_c,
    }
    return render(request, 'contact.html', context)
