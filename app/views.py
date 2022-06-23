from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic

from .forms import CardForm
from .models import Card


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
        card = form.save()

        if self.request.headers.get('HX-Request'):
            return render(self.request, 'layout/_card.html', {'card': card})
        return redirect('home')

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors.as_text()}, status=400)
