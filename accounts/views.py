
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Profile
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

class DetailProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/detailprofile.html"
		profilee = User.objects.get(username=request.user)
		detail = Profile.objects.get(user=request.user)
		context = {
		'profilee':profilee,
		'detail':detail,
		}
		return render(request,template_name,context)


class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		'userform':userform,
		'profileform':profileform,
		}
		return render(request,template_name,context)
		
	def post(self,request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user,data=request.POST)
		profileform = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			return redirect('profile')
		else:
			context={
			'userform':userform,
			'profileform':profileform,
			}
			return render(request,template_name,context)
		

class Registration(View):
	def get(self, request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			# perfil = Profile(instance=new_user)
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			# perfil = Profile.objects.create(user=new_user)
			return redirect('profile')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)




