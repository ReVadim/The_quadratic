from django.db import models


class TimestampFields(models.Model):
    """ Date and time information """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    class Meta:
        abstract = True


class SolvingEquation(TimestampFields, models.Model):
    """ We save the input parameters and the results of calculating the equation """

    params = models.CharField(verbose_name='Параметры', max_length=255)
    results = models.CharField(verbose_name='Результат', max_length=255)

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'
        ordering = ['-created_at']

    def __str__(self):
        return f'Params: {self.params}\nResults: {self.results}'


class Comments(TimestampFields, models.Model):
    """ Comments from users. Without authentication """

    username = models.CharField(verbose_name='Пользователь', max_length=50)
    comment_text = models.CharField(verbose_name='Комментарий', max_length=300)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return f'User: {self.username}\nComment{self.comment_text}'
