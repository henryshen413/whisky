import json
import urllib

from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import login as auth_login

class LoginAjaxMixin(object):
    """
    Mixin which authenticates user if request is an ajax request
    """

    def form_valid(self, form):
        if not self.request.is_ajax():
            auth_login(self.request, form.get_user(), backend='whiskysite.backends.EmailBackend')
            messages.success(self.request, self.success_message)

        return HttpResponseRedirect(self.get_success_url())

class NormalUserLoginMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            raise Http404

        return super(NormalUserLoginMixin, self).dispatch(request, *args, **kwargs)