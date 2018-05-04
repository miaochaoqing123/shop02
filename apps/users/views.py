from random import choice

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import  Smserializer
from utils.yunpian import YunPian
from MxShop.settings import APIKEY
from .models import VerifyCode

# Create your views here.

User = get_user_model()


class CustomBackend(ModelBackend):
    """自定义用户验证"""
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """发送短信验证码"""
    serializer_class = Smserializer

    def generate_code(self):
        """
        生成4位随机数
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        """
        验证码
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        yun_pian = YunPian(APIKEY)

        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status['code'] != 0:
            return Response(
                {'mobile':sms_status['msg']},
                status=status.HTTP_400_BAD_REQUEST)

        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response(
                {'mobile':mobile},
                status=status.HTTP_201_CREATED)

