from django.conf.urls import url
from User import views
app_name = 'user'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^change_password/$', views.ChangePasswordView, name="change_password"),
    url(r'^profile/$', views.uprofile, name='profile'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
