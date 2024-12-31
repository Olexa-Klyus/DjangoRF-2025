from django_filters import rest_framework as filters


class AdvertsFilters(filters.FilterSet):
    year_from = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_to = filters.NumberFilter(field_name='year', lookup_expr='lte')
    region_in = filters.BaseInFilter(field_name='region')
    city_in = filters.BaseInFilter(field_name='city')
    
    order = filters.OrderingFilter(
        fields=(
            'year',
            'price',
            'mileage',
            'updated_at'
        )
    )
