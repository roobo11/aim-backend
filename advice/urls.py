from django.urls import path
from .views import AdviceRequestView, PortfolioListView

urlpatterns = [
    path("", AdviceRequestView.as_view(), name="advice-request"),
    path("portfolios/", PortfolioListView.as_view(), name="portfolio-list"),
]