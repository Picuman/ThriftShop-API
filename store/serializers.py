from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ItemSerializer(serializers.ModelSerializer):
    seller_username = serializers.ReadOnlyField(source='seller.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = [
            'id', 'seller_username', 'title', 'description', 
            'price', 'condition', 'size', 'image', 
            'category', 'category_name', 'created_at', 'is_sold'
        ]
        read_only_fields = ['seller', 'created_at', 'is_sold']

    def create(self, validated_data):
        # Automatically set the seller to the current logged-in user
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)