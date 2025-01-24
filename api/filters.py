# import django_filters
# from datka_app.models import News

# class NewsFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')  # Нечувствительный к регистру и частичное совпадение
#     content = django_filters.CharFilter(lookup_expr='icontains')  # Нечувствительный к регистру и частичное совпадение

#     class Meta:
#         model = News
#         fields = ["name", "cont"]