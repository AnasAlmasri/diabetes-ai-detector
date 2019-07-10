"""RetinaScreener URL Configuration

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
from django.urls import path
from django.urls import include
from RetinaScrApp import views
from RetinaScrApp.views import requestAjax, compileCode
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('RetinaScrApp/', include('RetinaScrApp.urls')),
    path('new_user', views.new_user, name='new_user'),
    path('diagnosis', views.diagnosis, name='diagnosis'),
    path('customize_algorithm', views.customize_algorithm, name='customize_algorithm'),
    path('new_algorithm', views.new_algorithm, name='new_algorithm'),
    path('how_it-works', views.how_it_works, name='how_it_works'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('data_ajax_request', requestAjax, name='data_ajax_request'),
    path('code_editor_ajax_request', compileCode, name='code_editor_ajax_request'),
    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
