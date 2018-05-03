from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import GoodsSerializer
from .models import Goods

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """自定义page"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表项
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

















