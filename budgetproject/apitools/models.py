from datetime import datetime

from django.db import models


TYPE_URL_BUDGET = [
    ('budget', 'budget'),
    ('glavbudget', 'glavbudget'),
]

class Url(models.Model):
    """ Модель для импорта данных """
    url = models.URLField()
    type_budget = models.CharField(
        max_length=30, choices=TYPE_URL_BUDGET, default='budget')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.type_budget}'

    class Meta:
        verbose_name = 'Ссылка для запроса'
        verbose_name_plural = 'Ссылки для запросов'
