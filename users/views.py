from django.views.generic.edit import CreateView
from users.forms import UserForm
# Create your views here.


class UserRegisterView(CreateView):
    form_class = UserForm
    template_name = 'user_register.html'
