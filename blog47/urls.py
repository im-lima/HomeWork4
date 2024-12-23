"""
URL configuration for blog4 project.

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
from django.conf.urls.static import static
from django.conf import settings
from posts.views import (
    main_view,
    posts_list_view,
    post_detail_view,
    post_create_view,
)
from user.views import register_view, login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="home"),
    path("posts/", posts_list_view, name="posts_list"),
    path("posts/<int:pk>/", post_detail_view, name="post_detail"),
    path("posts/create/", post_create_view, name="post_create"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)