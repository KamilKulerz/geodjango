from django.urls import path
from shops_app import views

urlpatterns = [
    # [...]
    path("", views.Home.as_view())
]
