from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
        New message: {}

        From: {}

        '''. format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['igorcury210@gmail.com'])

    return render(request, 'index.html')

def contato(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
        New message: {}

        From: {}

        '''. format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [''])

    return render(request, 'contato.html')
     
def projeto(request):
    return render(request, 'projeto.html')

def sobre(request):
    return render(request, 'sobre.html')
