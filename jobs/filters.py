import django_filters
from .models import Jobs

class JobsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Jobs
        fields = ['title','description',]