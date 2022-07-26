"""hamzoooz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# from django.urls import include, path
# from other_app.views import Home
# from my_app import views

from django.contrib import admin
from django.urls import path

urlpatterns = [

    path(r'^$', 'blogs.views.home', name='home'),
    # path('D:\Programming\learn\#006_python\#004_Django_M Essa\hamzoooz',  blog.view.home, name='Home'),
    path('admin/', admin.site.urls),
]
