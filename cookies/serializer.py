from rest_framework import serializers
from .models import CookieStand


class CookieStandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'location', 'owner', 'description', 'hourly_sales', 'maximum_customers_per_hour',
            'minimum_customers_per_hour', 'average_cookies_per_sale'
        )
        model = CookieStand
