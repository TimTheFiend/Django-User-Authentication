from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    """ `reverse` and `reverse_lazy` essentially goes into the
     `urls.py` and finds the match based on name.
      """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
