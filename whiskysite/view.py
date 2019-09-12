import csv

from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.auth import logout
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

from io import TextIOWrapper, StringIO

from whiskysite.form import *
from whiskysite.mixin import *
from whiskydatabase.models import UserRole, Distillery, Country, Region, Comment, Wishlist




class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
	authentication_form = CustomAuthenticationForm
	template_name = 'login.html'
	success_message = '登入成功'

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

class SignUpView(SuccessMessageMixin, CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_message = 'Sign up succeeded. Please verify your email.'

	def form_valid(self, form):
		if not self.request.is_ajax():
			user = form.save()
			UserRole.objects.create(user=user, role="User")

		return HttpResponse('success')

class UserWineRatingView(NormalUserLoginMixin, TemplateView):
	template_name = 'user/user_profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_comment = Comment.objects.filter(user=self.request.user).order_by('created_at')
		context.update({
            "user_comment": user_comment,
        })
		return context

class UserWineWishlistView(NormalUserLoginMixin, TemplateView):
	template_name = 'user/user_profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_wishlist = Wishlist.objects.filter(user=self.request.user).order_by('created_at')
		context.update({
			"user_wishlist": user_wishlist,
        })
		return context


def upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			distillery, created = Distillery.objects.get_or_create(name=line[0], country=Country.objects.get(name=line[3]), region=Region.objects.get(name=line[4]))
			if line[8] != "":
				distillery.lat = line[8]
			if line[7] != "":
				distillery.lon = line[7]
			distillery.name = line[0]
			distillery.slug = line[1]
			distillery.owner = line[2]
			if line[5] != "":
				distillery.year_founded = line[5]
			distillery.description = line[6]
			distillery.is_active = line[9]

			distillery.save()

		return render(request, 'upload.html')

	else:
		return render(request, 'upload.html')