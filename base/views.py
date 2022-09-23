from django.views.generic import TemplateView
from django.core.mail import send_mail

# Create your views here.
class IndexView(TemplateView):
  template_name = 'base/index.html'

  def post(self, request, *args, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    ms = request.POST.get('message')

    message = name + " - " + ms    

    send_mail(subject, message, email, ['marcosmontielrej@gmail.com'])