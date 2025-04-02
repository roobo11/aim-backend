from django.urls import path
from .views import SecurityListCreateView, SecurityUpdateDeleteView

urlpatterns = [
    path("", SecurityListCreateView.as_view(), name="security-list-create"),
    path("<int:pk>/", SecurityUpdateDeleteView.as_view(), name="security-update-delete"),
]