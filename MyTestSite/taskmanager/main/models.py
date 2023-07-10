from django.db import models


class Task(models.Model):
    objects = ' '
    title = models.CharField('Название', max_length=70)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
