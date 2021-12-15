import django_filters
from owner.models import Mobile


class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobile
        fields = ["mobile_name", "company", "price"]
