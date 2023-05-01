from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import UserForm
from users.models import Users
from users.services import persist_user
# Create your views here.


class UserRegisterView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'user_register.html'

    def post(self, request, *args, **kwargs):
        '''
            Validate obtained form fields and 
            persist user and redirect to user_login
            * If they email are already registered
              render user_error.html template
        '''
        form = self.get_form()
        if (form.is_valid()):
            persisted_user = persist_user(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return redirect(
                reverse_lazy('user_login')
            )
        return render(request, 'user_error.html')
