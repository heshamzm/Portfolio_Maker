from django.views.generic.base import RedirectView
from .forms import UserForm, NameForm
from django.views.generic.edit import FormView

# Create your views here.




class home(FormView):
    form_class = UserForm
    template_name = "home.html" 
    success_url = "name"

    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)

class name(FormView):
    form_class = NameForm
    template_name = "name.html"
    success_url = "/"

    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)