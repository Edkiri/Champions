# Users urls

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
  path('signup/', views.SignupView.as_view(), name='signup'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  path('me/profile', views.ProfileUpdateView.as_view(), name='update'),
	path(
		route='<str:username>', 
		view=views.UserDetailView.as_view(),
		name='detail'
  ),
]