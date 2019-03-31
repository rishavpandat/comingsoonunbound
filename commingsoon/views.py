from django.views.generic.edit import CreateView
from .models import SoonModel
from django.contrib.messages.views import SuccessMessageMixin

class SoonView(SuccessMessageMixin, CreateView):
    model = SoonModel
    fields = ['name', 'business_name', 'number', 'email', ]
    template_name = 'commingsoon/soon.html'
    success_url = '/'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Your form has been submited"