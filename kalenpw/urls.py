"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from rss.views import generate_rss

from core import views

import core.views

admin.site.site_header = "blog.kalen.pw admin"
admin.site.site_title = "blog.kalen.pw"


urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="core/robots.txt", content_type="text/plain")),
    path('', include('blog.urls')),
    path('', views.index, name='index'),
    path('rss/', generate_rss, name='rss'),
    path('account/', include('accounts.urls')),
    # password reset
    path(
        'reset',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'
    ),
    path(
        'reset/done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    # account


    path('aadmin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),

    path('404', views.error_404)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
