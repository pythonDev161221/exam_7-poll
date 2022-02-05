from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.question}{self.created_at}'


class Choice(models.Model):
    answer = models.CharField(max_length=200)
    poll = models.ForeignKey('webapp.Poll', related_name='choices',
                             on_delete=models.CASCADE, verbose_name='Ответы')

    def __str__(self):
        return f'{self.answer}'

