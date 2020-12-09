import requests

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Url
from budget.serializers import BudgetValidateSerrializer, GlavBudgetValidateSerializer
from budget.models import Budget, GlavBudgetClass


def response_data(url):
    """ Получаем данные в виде списка """
    r = requests.get(url)
    response_data = r.json()
    page_range = response_data['pageSize']
    return response_data


def glav_budget(curent_data):
    """ Для обработки модели GlavBudgetClass """
    serializer_glavbudget = GlavBudgetValidateSerializer(
        data=curent_data)
    if serializer_glavbudget.is_valid(raise_exception=False):

        code = serializer_glavbudget.validated_data['code']
        glavbudget_ = serializer_glavbudget.validated_data
        glavbudget, created = GlavBudgetClass.objects.update_or_create(
            code=code, defaults=glavbudget_)
    return Response({'test message': 'test'}, status=status.HTTP_200_OK)


def budget(curent_data):
    """ Для обработки модели Budget """
    parentcode = curent_data.pop('parentcode')
    code = curent_data['code']

    serializer_budget = BudgetValidateSerrializer(data=curent_data)
    if serializer_budget.is_valid(raise_exception=False):

        code = serializer_budget.validated_data['code']
        budget_ = serializer_budget.validated_data
        budget, created = Budget.objects.update_or_create(
            code=code, defaults=budget_)
        try:
            # получаем в БД бюджет по code
            a = Budget.objects.get(code=code)
            # получаем бюджет чей code равен parentcode
            b = Budget.objects.get(code=parentcode)
            # приставеваем родителя
            a.parentcode = b
            a.save()
        except Budget.DoesNotExist:
            pass


@receiver(post_save, sender=Url)
def get_data(sender, instance, **kwargs):
    """ Обработка ссылки """
    url = instance.url
    data = response_data(str(url))
    received_data = data['data']
    for i in range(len(received_data)):
        curent_data = received_data[i]

        if instance.type_budget == 'budget':
            budget(curent_data)

        elif instance.type_budget == 'glavbudget':
            glav_budget(curent_data)
