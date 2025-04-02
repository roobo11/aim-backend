from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Security
from .serializers import SecuritySerializer

class SecurityListCreateView(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    permission_classes = [IsAuthenticated]

class SecurityUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    permission_classes = [IsAuthenticated]
