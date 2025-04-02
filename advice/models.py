from django.db import models
from django.conf import settings
from securities.models import Security

class Portfolio(models.Model):
    RISK_TYPE = [(1, "공격형"), (2, "중립형")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.IntegerField(choices=RISK_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

class PortfolioItem(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='items')
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.IntegerField()