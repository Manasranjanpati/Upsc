"""ManasUPSC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from upscapp.views import *
from User.views import *
app_name = "upscapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/',homeview),
    # path('success/',successview),
    #path('', views.homeview),
    path('services/', servicesview),
    path('contact/', contactview),
    path('gallary/', gallaryview),
    path('feedback/', feedbackview),
    path('post/', post_list),
    path('post_create/', postcreation_view),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('user/', include('User.urls', namespace="user")),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)