from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # 기본 User 모델 사용, 필요 시 확장 가능

class LoginHistory(models.Model):
    ACTIONS = [("login", "로그인"), ("logout", "로그아웃")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(choices=ACTIONS, max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

class Transaction(models.Model):
    TYPE_CHOICES = [("deposit", "입금"), ("withdraw", "출금")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
