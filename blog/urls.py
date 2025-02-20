"""
URL configuration for blog project.

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
from django.contrib import admin
from django.urls import path
from posts.views import post_view, text_view, main_page, post_create_view, post_detail_view
from django.conf.urls.static import static
from django.conf import settings
from user.views import register_view, login_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_view, name='posts'),
    path('text/', text_view, name="text"),
    path('', main_page, name='main_page'),
    path('posts/<int:post_id>/', post_detail_view, name='post-detail'),
    path('posts/create/', post_create_view, name="post_create"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)