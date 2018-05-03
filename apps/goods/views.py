from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import GoodsSerializer
from .models import Goods
from .filters import GoodsFilter

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """自定义page , 分页"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表项, 分页, 搜索, 过滤, 排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')  # 搜索, 过滤
    ordering_fields = ('sold_num', 'add_time')  # 排序


















