"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from libraryapp import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('studentsignup', views.studentsignup_view),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html')),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('afterlogin', views.afterlogin_view),
    path('addbook',views.addbook_view),
    path('viewbook',views.viewbook_view),
    path('issuebook',views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent',views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent,name='viewissuedbookbystudent'),
    path('returnbook/<int:id>/', views.returnbook, name='returnbook'),
    path('aboutus', views.aboutus_view),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)