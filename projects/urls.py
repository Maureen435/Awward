from django.urls import path
from . import views
from .views import PostListView,PostDetailView,SignUpView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
