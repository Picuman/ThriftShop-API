from rest_framework import generics
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

# View for listing all categories or creating a new one
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Add this method:
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)