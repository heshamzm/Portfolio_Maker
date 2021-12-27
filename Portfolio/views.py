
from .forms import UserForm
from django.views.generic.edit import FormView
# Create your views here.




class home(FormView):
    form_class = UserForm
    template_name = "home.html" 
    success_url = "/" 

    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)