from rest_framework import serializers
from .models import Budget, GlavBudgetClass


class BudgetValidateSerrializer(serializers.ModelSerializer):
    """ Для валидации модели Budget """

    class Meta:
        model = Budget
        fields = [
            'code',
            'name',
            'parentcode',
            'startdate',
            'status',
            'budgtypecode']


class GlavBudgetValidateSerializer(serializers.ModelSerializer):
    """ Для валидации модели GlavBudgetClass """

    class Meta:
        model = GlavBudgetClass
        fields = [
            'code',
            'name',
            'startdate',
        ]
