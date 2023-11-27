from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    """ A view to return contact page and submit contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success_page')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success_page(request):
    """ A view to return contact success page """

    return render(request, 'contact/contact_success_page.html')
