from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from decimal import Decimal

from accounts.models import Account
from .models import Portfolio, PortfolioItem
from .serializers import PortfolioSerializer
from securities.models import Security

class AdviceRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            risk_type = int(request.data.get("type"))
            if risk_type not in [1, 2]:
                return Response({"error": "위험도는 1 또는 2여야 합니다."}, status=400)

            account = Account.objects.select_for_update().get(user=request.user)
            if risk_type == 1:
                use_amount = account.balance
            else:
                use_amount = account.balance * Decimal("0.5")

            securities = list(Security.objects.all().order_by('price'))
            if not securities:
                return Response({"error": "사용 가능한 증권이 없습니다."}, status=400)

            portfolio = Portfolio.objects.create(user=request.user, type=risk_type)
            remaining = use_amount
            used_total = Decimal("0")

            for sec in securities:
                if sec.price > remaining:
                    continue
                qty = int(remaining // sec.price)
                if qty == 0:
                    continue
                PortfolioItem.objects.create(
                    portfolio=portfolio,
                    security=sec,
                    quantity=qty
                )
                cost = sec.price * qty
                used_total += cost
                remaining -= cost

            account.balance -= used_total
            account.save()

            return Response({
                "message": "자문 요청이 완료되었습니다.",
                "사용금액": float(used_total),
                "남은금액": float(account.balance),
                "포트폴리오ID": portfolio.id
            })
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class PortfolioListView(generics.ListAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user).order_by('-created_at')
