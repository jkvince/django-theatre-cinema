from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from accounts.models import CustomUser


class AdminBaseView(PermissionRequiredMixin):
	# Abstract class for admin pages
	permission_required = 'accounts.CustomUser'
	raise_exception = True
	login_url = 'accounts/login'


class AdminMainView(AdminBaseView, TemplateView):
	template_name = 'main.html'

class AdminUserView(AdminBaseView, TemplateView):
	template_name = 'user.html'
	model = CustomUser
	context_object_name = 'user_list'

	#def get_queryset(self):
	#	query = self.request.GET.get('q')
	#	if query:  # Ensure query is not None or empty
	#	    return CustomUser.objects.filter(
	#	        Q(name__icontains=query) | Q(description__icontains=query)
	#	    )
	#	return CustomUser.objects.all()
	#
	#def get_context_data(self, **kwargs):
	#	context = super(AdminUserView,self).get_context_data(**kwargs)
	#	context['query'] = self.request.GET.get('q')
	#	return context