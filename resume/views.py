from django.shortcuts import render
from . import models
from .forms import ContatUS
from django.views.generic.detail import DetailView

# Create your views here.

def portfolio(request):
    home = models.Home.objects.all()
    portfolio = models.Portfolio.objects.all()
    form = ContatUS()
    if request.method == 'POST':
        form = ContatUS(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            contact = models.Contact(
                name = name,
                email= email,
                message = message
            )
            contact.save()
    context = {
        'home':home,
        'portfolio':portfolio,
        'form':form
    }
    return render(request, 'index.html',context)

class portfolioDetailView(DetailView):
    model = models.Portfolio
    template_name = "gallery.html"
    context_object_name = 'obj'

    def Query_set(self):
        return models.portfolioImg.objects.filter(portfolio=models.Portfolio)