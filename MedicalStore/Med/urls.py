from django.urls import path
from Med import views
from django.contrib.auth import views as av

urlpatterns = [
	path('',views.home,name="hm"),
	path('lgn/',av.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgot/',av.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
	path('reg/',views.register,name="rg"),
	path('mn/',views.mainpage,name="mnp"),
	path('usrq/',views.usercrdntls,name="usc"),
	path('prm/',views.peruser,name="pmu"),
	path('eper/<int:k>/',views.gvper,name="gp"),
]