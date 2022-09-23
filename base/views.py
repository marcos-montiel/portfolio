from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import EmailForm

# Create your views here.
class IndexView(FormView):
  template_name = 'base/index.html'
  form_class = EmailForm
  success_url = reverse_lazy('index')
