from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect("/api/")  # change to your actual base endpoint if different

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),  # or however you wired it
]
