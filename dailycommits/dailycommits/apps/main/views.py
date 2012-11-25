from django.views.generic import TemplateView, RedirectView

class MainView(TemplateView):
    template_name = 'main/main.html'

