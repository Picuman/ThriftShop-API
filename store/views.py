from rest_framework import viewsets, permissions, filters
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public View: List all categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class ItemViewSet(viewsets.ModelViewSet):
    """
    CRUD View:
    - List/Retrieve: Allow Any (Public)
    - Create/Update/Delete: Authenticated Users only
    """
    queryset = Item.objects.filter(is_sold=False) 
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'category__name']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]