"""
URL configuration for pythonse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from page.views import (login_view,register_view,dashboard_view,logout_view,contact_view,about_view,concert_view_UT,
                        post_comment,ticket_view,purchase_view,concert_view_RS,concert_view_WM,user_profile,concert_view_EC)

urlpatterns = [
    path('', dashboard_view),
    path('/', dashboard_view, name='home'),
    path('login/', login_view, name='login'),
    path('purchase-success/', purchase_view, name='purchase-success'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('about-us/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('concert-pages/untold/<int:event_id>/', concert_view_UT, name='concert-untold'),
    path('concert-pages/rockstadt/<int:event_id>/', concert_view_RS, name='concert-rockstadt'),
    path('concert-pages/WM/<int:event_id>/', concert_view_WM, name='concert-WM'),
    path('concert-pages/EC/<int:event_id>/', concert_view_EC, name='concert-EC'),
    path('ticket/<int:event_id>/', ticket_view, name='ticket'),
    path('front_page/', dashboard_view, name='front-page'),
    path('post_comment/', post_comment, name='post_comment'),
    path('profile/', user_profile, name='user-profile'),
    path('admin/', admin.site.urls),
]
