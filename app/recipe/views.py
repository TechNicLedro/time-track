"""
Views for the recipe API
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View to manage recipe APIs"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_class = [TokenAuthentication]
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        """Retrive recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')