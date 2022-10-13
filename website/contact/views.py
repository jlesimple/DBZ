from django.shortcuts import render, redirect
from django.core.mail import send_mail

from contact.forms import ContactUsForm

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via DBZ_website  Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@admin.lan'],
            )
            return redirect('email-sent')
    else :
        form = ContactUsForm()
    return render(request, 'contact/contact.html', {'form': form})
