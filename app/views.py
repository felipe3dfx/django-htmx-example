from django.shortcuts import redirect
from django.views import generic

from .models import Card
from .forms import CardForm


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'cards': Card.objects.all(),
            'form': CardForm,
        })
        return context


class CardCreateView(generic.CreateView):
    model = Card
    form_class = CardForm

    def form_valid(self, form):
        form.save()
        return redirect('home')
