from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from MyOlimp.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import SuggestionForm


def mainpage(request):
    data = {
        'title': 'MyOlimp Главная'
    }
    return render(request, 'main/mainpage.html', data)


def suggestion_view(request):
    if request.method == 'GET':
        form = SuggestionForm()
    elif request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {email}', message, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос')
    return render(request, 'main/suggestion.html', {'form': form})


def success_view(request):
    return render(request, 'main/sendmessage.html')
