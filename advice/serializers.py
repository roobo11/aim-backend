from rest_framework import serializers
from .models import Portfolio, PortfolioItem
from securities.serializers import SecuritySerializer

class PortfolioItemSerializer(serializers.ModelSerializer):
    security = SecuritySerializer()

    class Meta:
        model = PortfolioItem
        fields = ['security', 'quantity']

class PortfolioSerializer(serializers.ModelSerializer):
    items = PortfolioItemSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'type', 'created_at', 'items']