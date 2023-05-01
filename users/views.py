from django.shortcuts import render
from django.views.generic.edit import CreateView
from users.forms import UserForm
from users.models import Users
# Create your views here.


class UserRegisterView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'user_register.html'

    def post(self, request, *args, **kwargs):
        '''
            Validate obtained form fields and 
            persist user
            * If they email are already registered
              render user_error.html template
        '''
        return render(request, 'user_error.html')
