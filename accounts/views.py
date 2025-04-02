from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, TransactionSerializer, BalanceSerializer
from .models import User, LoginHistory, Account, Transaction
from decimal import Decimal

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = User.objects.get(username=request.data['username'])
            LoginHistory.objects.create(user=user, action="login")
        return response

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            LoginHistory.objects.create(user=request.user, action="logout")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DepositView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount')
        if not amount:
            return Response({"error": "입금 금액이 필요합니다."}, status=400)
        account = Account.objects.get(user=request.user)
        account.balance += Decimal(amount)
        account.save()
        Transaction.objects.create(user=request.user, type='deposit', amount=amount)
        return Response({"message": "입금 완료", "balance": account.balance})

class WithdrawView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        amount = request.data.get('amount')
        if not amount:
            return Response({"error": "출금 금액이 필요합니다."}, status=400)
        account = Account.objects.get(user=request.user)
        if account.balance < Decimal(amount):
            return Response({"error": "잔고 부족"}, status=400)
        account.balance -= Decimal(amount)
        account.save()
        Transaction.objects.create(user=request.user, type='withdraw', amount=amount)
        return Response({"message": "출금 완료", "balance": account.balance})

class BalanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        account = Account.objects.get(user=request.user)
        serializer = BalanceSerializer(account)
        return Response(serializer.data)
