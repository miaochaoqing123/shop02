# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.views.generic.base import View

from goods.models import Goods
# from django.views.generic import ListView

class GoodsListView(View):
    def get(self,request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        # from django.forms.models import model_to_dict  # 可以取代上面的代码,优化代码
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        import json
        from django.core import serializers  # 用于序列化
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        # 当使用HttpResponse时,可以把上面的json_data = json.loads(json_data) 注释掉
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(json_data, safe=False)











