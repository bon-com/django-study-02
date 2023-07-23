from django.contrib import admin
from django.urls import path
from .views import HelloWorldClass, hello2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello1/", HelloWorldClass.as_view()),
    path("hello2/", hello2),
]
