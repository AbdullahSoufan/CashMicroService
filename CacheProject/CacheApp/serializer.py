from rest_framework import serializers
from .models import Cache

class bookSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = ('title', 'quantity', 'price', 'topic')
