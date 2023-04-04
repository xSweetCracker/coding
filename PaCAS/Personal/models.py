from django.db import models


# Create your models here.
class Personal(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Имя'
    )
    is_taskmaster = models.BooleanField(
        default=False,
        null=True,
        verbose_name='Начальник участка'
    )
    is_master = models.BooleanField(
        default=False,
        null=True,
        verbose_name='Мастер'
    )

    def __str__(self):
        if self.is_taskmaster:
            return f'{self.name} - Начальник участка'
        elif self.is_master:
            return f'{self.name} - Мастер'
        else:
            return f'{self.name}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Brigade(models.Model):
    brigade_id = models.PositiveIntegerField(
        verbose_name='ID рабочей команды'
    )
    workers = models.ForeignKey(
        'Personal',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Закрепленные работники'
    )

    def __str__(self):
        return f'#{self.brigade_id}'

    class Meta:
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'


class ObjWorks(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название объекта'
    )
    works_brigade = models.ForeignKey(
        'Brigade',
        max_length=64,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Рабочая бригада'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объект работ'
        verbose_name_plural = 'Объекты работ'