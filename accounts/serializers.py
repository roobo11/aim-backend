from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Account, Transaction

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        Account.objects.create(user=user)
        return user

# 잔고 확인
class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["balance"]

# 입출금 기록
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "type", "amount", "created_at"]
