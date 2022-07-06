from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    """
    A view to return the home page
    """
    return render(request, 'pages/index.html')


# Original Code with modifications from https://bit.ly/3BM12q2
def contact_view(request):
    """
    A view to return the contact form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [
                    'contact@sarancollection.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home/contact_us.html", {'form': form})


def success_view(request):
    """
    A view to return the success page after an email was sent.
    """
    return render(request, 'home/contact_success.html')