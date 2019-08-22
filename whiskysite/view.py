from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import *
from django.contrib.auth.views import LoginView

from whiskysite.form import *
from whiskydatabase.models import UserRole


class CustomLoginView(SuccessMessageMixin, LoginView):
	authentication_form = CustomAuthenticationForm
	template_name = 'login.html'
	success_message = '登入成功'

	def login(self, request):
		return HttpResponseRedirect(request.GET.get('next'))

class SignUpView(SuccessMessageMixin, CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_message = 'Sign up succeeded. Please verify your email.'

	def form_valid(self, form):
		if not self.request.is_ajax():
			user = form.save()
			UserRole.objects.create(user=user, role="User")
			UserProfile.objects.create(user=user)

			current_site = get_current_site(self.request)
			mail_subject = '啟用您的 Blockore 帳號'
			message = render_to_string('emails/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode,
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			if not settings.DEBUG:
				email.send()

			return HttpResponseRedirect('/email_verification_notify')
		return HttpResponse('success')