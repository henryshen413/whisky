from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect

from whiskysite.form import *
from whiskysite.mixin import *
from whiskydatabase.models import UserRole


class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
	authentication_form = CustomAuthenticationForm
	template_name = 'login.html'
	success_message = '登入成功'

class SignUpView(SuccessMessageMixin, CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_message = 'Sign up succeeded. Please verify your email.'

	def form_valid(self, form):
		if not self.request.is_ajax():
			user = form.save()
			UserRole.objects.create(user=user, role="User")

		return HttpResponse('success')