from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Participants(TemplateView):
    template_name = 'participants.html'

class Journal(TemplateView):
    template_name = 'journal.html'

class Resources(TemplateView):
    template_name = 'resources.html'
