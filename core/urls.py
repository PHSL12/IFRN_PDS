from django.contrib import admin
from django.urls import path

from .views import jackson_view, pedro_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("jackson/", jackson_view, name="jackson"),
    path("pedro/", pedro_view, name="pedro"),
]
