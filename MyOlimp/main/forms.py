from django import forms


class SuggestionForm(forms.Form):
    email = forms.EmailField(label='', initial='Ваш Email', required=True)
    subject = forms.CharField(label='', initial='Тема вашего сообщения', required=True)
    message = forms.CharField(label='', initial='Сообщение для администрации сайта', widget=forms.Textarea, required=True)
