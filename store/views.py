from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer, UserRegistrationSerializer

# --- AUTH VIEWS ---

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# --- CATEGORY VIEWS ---

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# --- ITEM VIEWS ---

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]